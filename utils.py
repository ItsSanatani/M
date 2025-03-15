from pyrogram.raw.types import (
    InputReportReasonOther, InputReportReasonSpam, InputReportReasonViolence,
    InputReportReasonChildAbuse, InputReportReasonPornography, InputReportReasonCopyright,
    InputReportReasonFake, InputReportReasonIllegalDrugs, InputReportReasonPersonalDetails
)

def get_report_reason(reason: str):
    reasons_map = {
        "spam": InputReportReasonSpam(),
        "violence": InputReportReasonViolence(),
        "child_abuse": InputReportReasonChildAbuse(),
        "pornography": InputReportReasonPornography(),
        "copyright": InputReportReasonCopyright(),
        "fake": InputReportReasonFake(),
        "illegal": InputReportReasonIllegalDrugs(),
        "personal": InputReportReasonPersonalDetails(),
        "other": InputReportReasonOther(),
    }
    return reasons_map.get(reason, InputReportReasonOther())
