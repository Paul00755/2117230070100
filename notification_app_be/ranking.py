#import date & time
from datetime import datetime


weights = {
    "Placement": 100,
    "Result": 70,
    "Event": 40
}


def calculate_score(notification):

    notification_type = notification.get(
        "Type",
        "Other"
    )

    base_score = weights.get(
        notification_type,
        10
    )

    timestamp_string = notification.get(
        "Timestamp",
        "2026-01-01 00:00:00"
    )

    timestamp = datetime.strptime(
        timestamp_string,
        "%Y-%m-%d %H:%M:%S"
    )

    recency_bonus = (
        timestamp.timestamp() / 100000000
    )

    return base_score + recency_bonus


def rank_notifications(notifications):

    scored = []

    for notification in notifications:

        score = calculate_score(notification)

        scored.append({
            "score": score,
            "notification": notification
        })

    scored.sort(
        reverse=True,
        key=lambda x: x["score"]
    )

    return scored[:10]