import datetime

def format_ics_datetime(dt):
    return dt.strftime("%Y%m%d")

def build_calendar():
    # Schedule of Oktagon MMA events with Main Event fight titles
    events = [
        {
            "num": "61",
            "main_event": "Machaev VS. Siraj",
            "location": "Brno, Czech Republic",
            "date": "2026-09-21"
        },
        {
            "num": "62",
            "main_event": "Eckerlin VS. Jungwirth",
            "location": "Frankfurt, Germany",
            "date": "2026-10-12"
        },
        {
            "num": "63",
            "main_event": "Vémola VS. Langer",
            "location": "Bratislava, Slovakia",
            "date": "2026-11-09"
        },
        {
            "num": "64",
            "main_event": "Moeil VS. Todev",
            "location": "Munich, Germany",
            "date": "2026-12-07"
        },
        {
            "num": "65",
            "main_event": "Kincl VS. Engizek",
            "location": "Prague, Czech Republic",
            "date": "2026-12-29"
        },
        {
            "num": "69",
            "main_event": "Kincl VS. Humburger",
            "location": "Ostrava, Czech Republic",
            "date": "2027-01-30"
        },
    ]

    ics_lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Oktagon MMA iCal Generator//EN",
        "X-WR-CALNAME:Oktagon MMA Events",
        "X-WR-TIMEZONE:UTC",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH"
    ]

    for event in events:
        event_dt = datetime.datetime.strptime(event["date"], "%Y-%m-%d").date()
        start_str = format_ics_datetime(event_dt)
        end_str = format_ics_datetime(event_dt + datetime.timedelta(days=1))
        
        # Formats title strictly as: "🥊 OKTAGON <Num>: <Main Event>"
        event_title = f"🥊 OKTAGON {event['num']}: {event['main_event']}"
        uid = f"OKTAGON_{event['num']}_{start_str}@oktagonmma"

        ics_lines.extend([
            "BEGIN:VEVENT",
            f"UID:{uid}",
            f"SUMMARY:{event_title}",
            f"DTSTART;VALUE=DATE:{start_str}",
            f"DTEND;VALUE=DATE:{end_str}",
            f"LOCATION:{event['location']}",
            f"DESCRIPTION:Main Event: {event['main_event']} ({event['location']})",
            "STATUS:CONFIRMED",
            "END:VEVENT"
        ])

    ics_lines.append("END:VCALENDAR")

    with open("oktagon-mma.ics", "w", encoding="utf-8") as f:
        f.write("\n".join(ics_lines))

if __name__ == "__main__":
    build_calendar()

