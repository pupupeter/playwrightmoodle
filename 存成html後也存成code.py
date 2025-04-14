import os
import asyncio
from dotenv import load_dotenv
from playwright.async_api import async_playwright
import google.generativeai as genai

# 載入 .env 變數
load_dotenv()
USERNAME = "41122061L"
PASSWORD = os.getenv("PASSWORD")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not PASSWORD:
    print("🔴 無法讀取 PASSWORD，請確認 .env 設定。")
if not GEMINI_API_KEY:
    print("🔴 無法讀取 GEMINI_API_KEY，請確認 .env 設定。")
else:
    print("✅ 成功讀取密碼與金鑰")

# 將原始內容與 Gemini 回覆合併輸出到 HTML
def write_full_html(content_html, gemini_reply, output_path="homework.html"):
    full_html = f"""
    <!DOCTYPE html>
    <html lang="zh-TW">
    <head>
        <meta charset="UTF-8">
        <title>作業四草稿</title>
        <style>
            body {{ font-family: "微軟正黑體", sans-serif; line-height: 1.6; padding: 20px; }}
            h1 {{ color: #0077cc; }}
            h2 {{ color: #cc0000; }}
            .section {{ margin-bottom: 30px; }}
            .box {{ border: 1px solid #ccc; padding: 15px; background-color: #f9f9f9; }}
        </style>
    </head>
    <body>
        <h1>作業四內容擷取 + Gemini 草稿生成</h1>

        <div class="section">
            <h2>📌 Moodle 原始內容：</h2>
            <div class="box">{content_html}</div>
        </div>

        <div class="section">
            <h2>🤖 Gemini 生成草稿：</h2>
            <div class="box">{gemini_reply.replace('\n', '<br>')}</div>
        </div>
    </body>
    </html>
    """

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_html)

    print(f"✅ 已整合並寫入 HTML：{output_path}")

# 將生成的程式碼存為 .py 檔案
# 將生成的內容存為 .py 檔案
def save_code_as_py(gemini_reply, output_path="generated_code.py"):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(gemini_reply)
    print(f"✅ 內容已儲存至：{output_path}")

# 主流程：自動抓資料 + 呼叫 Gemini 回答
async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        # 登入 Moodle
        await page.goto("https://moodle3.ntnu.edu.tw/login/index.php")
        await page.fill("input#username", USERNAME)
        await page.fill("input#password", PASSWORD)
        await page.click('button[type="submit"].btn.btn-primary')
        await page.wait_for_timeout(3000)

        # 點擊右上角頭像 -> 儀表板
        await page.click('a.dropdown-toggle.icon-no-margin')
        await page.click('a.dropdown-item.menu-action[href*="/my/"]')
        await page.wait_for_timeout(3000)

        # 點選課程「1132程式語言」
        elements = await page.query_selector_all('span.multiline')
        for element in elements:
            text = await element.inner_text()
            if "1132程式語言" in text:
                await element.click()
                print("✅ 進入課程：1132程式語言")
                break
        await page.wait_for_timeout(3000)

        # 點選「公告」
        elements = await page.query_selector_all('span.instancename')
        for element in elements:
            text = await element.inner_text()
            if "公告" in text:
                await element.click()
                print("✅ 進入公告區")
                break
        await page.wait_for_timeout(3000)

        # 點選「作業四規定」
        elements = await page.query_selector_all('a.p-3.p-l-0.w-100.h-100.d-block')
        for element in elements:
            text = await element.inner_text()
            if "作業四規定" in text:
                await element.click()
                print("✅ 開啟：作業四規定")
                break
        await page.wait_for_timeout(3000)

        # 擷取內容
        await page.wait_for_selector('div#post-content-643397', timeout=5000)
        content_html = await page.inner_html('div#post-content-643397')

        await browser.close()

        # 使用 Gemini 分析並生成作業草稿
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel("gemini-2.5-pro-exp-03-25")
        prompt = f"以下是 Moodle 上老師發布的作業說明，請幫我撰寫符合要求的作業草稿內容，並且要給出完整的程式碼，且要先給完整的程式碼之後再解釋：\n\n{content_html}"
        response = model.generate_content(prompt)
        gemini_reply = response.text

        print("\n📄 Gemini 回覆如下：\n")
        print(gemini_reply)

        # 寫入整合版 HTML
        write_full_html(content_html, gemini_reply)

        # 儲存程式碼為 .py 檔案
        save_code_as_py(gemini_reply)

# 執行
if __name__ == "__main__":
    asyncio.run(run())
