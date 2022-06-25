from django.db import models
from datetime import datetime, timezone

class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def get_duration(self):
        if self.leaved_at:
            self.duration = self.leaved_at - self.entered_at
        else:
            self.duration = datetime.now(timezone.utc) - self.entered_at
        return self.duration

    def format_duration(self):
        seconds = self.duration.total_seconds()
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        return f'{hours:02.0f}:{minutes:02.0f}'

    def is_visit_long(self, minutes=60):
        return self.duration.total_seconds() >= minutes*60
