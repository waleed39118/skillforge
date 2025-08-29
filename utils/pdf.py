# utils/pdf.py
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib import colors

def build_user_report(user):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    p.setFont("Helvetica-Bold", 16)
    p.drawString(2*cm, height - 2*cm, f"SkillForge Report - {user.username}")

    y = height - 3*cm
    p.setFont("Helvetica", 11)

    for skill in user.skills.all().order_by('name'):
        p.setFillColor(colors.black)
        p.drawString(2*cm, y, f"Skill: {skill.name} | Level: {skill.level} | Started: {skill.started_at or '-'}")
        y -= 0.6*cm

        last = skill.progress_logs.first()
        if last:
            p.setFillColor(colors.darkgreen)
            p.drawString(2.5*cm, y, f"Latest Progress: {last.percent}% - {last.note or ''} ({last.created_at.date()})")
            y -= 0.5*cm

        goals = skill.goals.all()
        done = goals.filter(status='DONE').count()
        pending = goals.exclude(status='DONE').count()
        p.setFillColor(colors.blue)
        p.drawString(2.5*cm, y, f"Goals: {goals.count()} (Done: {done}, Pending: {pending})")
        y -= 0.5*cm

        ach = skill.achievements.count()
        p.setFillColor(colors.purple)
        p.drawString(2.5*cm, y, f"Achievements: {ach}")
        y -= 0.8*cm

        if y < 3*cm:
            p.showPage()
            y = height - 2*cm
            p.setFont("Helvetica", 11)

    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    return pdf