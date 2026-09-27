import datetime

def format_ics_utc_datetime(dt):
    # Formats datetime as YYYYMMDDTHHMMSSZ for iCal
    return dt.strftime("%Y%m%dT%H%M%SZ")

def build_calendar():
    # Official Oktagon MMA event schedule sourced directly from oktagonmma.com
    events = [
        {
            "num": "94",
            "main_event": "Eckerlin VS. Kozma",
            "location": "Deutsche Bank Park, Frankfurt, Germany",
            "date": "2026-09-26"
        },
        {
            "num": "95",
            "main_event": "Kincl VS. Humburger",
            "location": "Mattoni Arena, Karlovy Vary, Czech Republic",
            "date": "2026-10-17"
        },
        {
            "num": "96",
            "main_event": "Gogoladze VS. Klinkhammer",
            "location": "SAP Garden, Munich, Germany",
            "date": "2026-10-31"
        },
        {
            "num": "97",
            "main_event": "Severino VS. Holzer",
            "location": "ZAG Arena, Hannover, Germany",
            "date": "2026-11-07"
        },
        {
            "num": "98",
            "main_event": "Legierski VS. Buchinger",
            "location": "WERK ARENA, Třinec, Czech Republic",
            "date": "2026-11-21"
        },
        {
            "num": "99",
            "main_event": "Dortmund",
            "location": "Westfalenhalle, Dortmund, Germany",
            "date": "2026-12-05"
        },
        {
            "num": "100",
            "main_event": "Prague",
            "location": "O2 arena, Prague, Czech Republic",
            "date": "2026-12-29"
        },
        {
            "num": "101",
            "main_event": "Stuttgart 2027",
            "location": "Hanns-Martin-Schleyer-Halle, Stuttgart, Germany",
            "date": "2027-01-16"
        },
        {
            "num": "102",
            "main_event": "Vienna 2027",
            "location": "Wiener Stadthalle, Vienna, Austria",
            "date": "2027-02-20"
        },
        {
            "num": "105",
            "main_event": "Bratislava 2027",
            "location": "Ondrej Nepela Arena, Bratislava, Slovakia",
            "date": "2027-05-01"
        },
        {
            "num": "107",
            "main_event": "Düsseldorf",
            "location": "MERKUR SPIEL-ARENA, Düsseldorf, Germany",
            "date": "2027-05-15"
        },
    ]

    ics_lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Oktagon MMA iCal Generator//EN",
        "X-WR-CALNAME:Oktagon MMA Events",
        "X-WR-TIMEZONE:Europe/Prague",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH"
    ]

    for event in events:
        # Base event date
        event_date = datetime.datetime.strptime(event["date"], "%Y-%m-%d").date()
        
        # Start at 18:00 (18:00 local time = 16:00 UTC during Daylight Saving, 17:00 UTC standard time)
        # Standardizing local 18:00 start / 23:00 end
        start_dt = datetime.datetime.combine(event_date, datetime.time(18, 0, 0))
        end_dt = datetime.datetime.combine(event_date, datetime.time(23, 0, 0))

        start_str = format_ics_utc_datetime(start_dt)
        end_str = format_ics_utc_datetime(end_dt)
        
        event_title = f"🥊 OKTAGON {event['num']}: {event['main_event']}"
        uid = f"OKTAGON_{event['num']}_{event['date']}@oktagonmma"

        ics_lines.extend([
            "BEGIN:VEVENT",
            f"UID:{uid}",
            f"SUMMARY:{event_title}",
            f"DTSTART:{start_str}",
            f"DTEND:{end_str}",
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
