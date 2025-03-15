import os

API_ID = int(os.getenv("API_ID", "28795512"))  
API_HASH = os.getenv("API_HASH", "c17e4eb6d994c9892b8a8b6bfea4042a")  
BOT_TOKEN = os.getenv("BOT_TOKEN", "7893027318:AAHrAT8VukzZq3xUtAZuOuF2sKhhCok8gDg")  
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://SachinSanatani:SACHINxSANATANI@sanatani.bnmsfbd.mongodb.net/?retryWrites=true&w=majority&appName=Sanatani")  

OWNER_ID = int(os.getenv("OWNER_ID", "7775584890"))
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS", "").split()))

REPORT_REASONS = {
    "spam": "InputReportReasonSpam",
    "violence": "InputReportReasonViolence",
    "child_abuse": "InputReportReasonChildAbuse",
    "pornography": "InputReportReasonPornography",
    "copyright": "InputReportReasonCopyright",
    "fake": "InputReportReasonFake",
    "illegal": "InputReportReasonIllegalDrugs",
    "personal": "InputReportReasonPersonalDetails",
    "other": "InputReportReasonOther",
}
