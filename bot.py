from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from stake_predictor import generate_smart_tiles
from config import BOT_TOKEN, ADMIN_ID
import asyncio
import datetime

vip_users = set()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎮 Welcome to Stake Mines Predictor Bot!\nUse /buyvip to access premium signals.")

async def buyvip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💸 To get VIP access, send ₹299 to UPI ID: yourupi@upi\nThen send screenshot here.")

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in vip_users and user_id != ADMIN_ID:
        await update.message.reply_text("❌ VIP Only! Use /buyvip to get access.")
        return

    safe_tiles = generate_smart_tiles()
    await update.message.reply_text(
        f"💣 Stake Mines Smart Prediction\n✅ Safe Tiles: {safe_tiles}\n📈 Accuracy: 95%"
    )

async def addsignal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id == ADMIN_ID:
        user_id = int(context.args[0])
        vip_users.add(user_id)
        await update.message.reply_text(f"✅ User {user_id} added to VIP.")
    else:
        
        await update.message.reply_text("❌ Admin only.")
async def auto_signal(context: ContextTypes.DEFAULT_TYPE):
    safe_tiles = generate_smart_tiles()
    for user_id in vip_users:
        await context.bot.send_message(
            chat_id=user_id,
            text=f"📡 Auto Stake Mines Signal\n✅ Safe Tiles: {safe_tiles}\n⏰ {datetime.datetime.now().strftime('%H:%M:%S')}"
        )
        
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("buyvip", buyvip))
app.add_handler(CommandHandler("signal", signal))
app.add_handler(CommandHandler("addvip", addsignal))  # /addvip <user_id>

print("🤖 Bot is running...")
app.run_polling()
