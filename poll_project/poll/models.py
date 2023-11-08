from django.db import models

# Create your models here.
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)
class Poll(models.Model):
    title = models.CharField(max_length=200, unique=True)
    question = models.CharField(max_length=250)
    active_until = models.DateTimeField(blank=True, null=True, verbose_name="Active until",)
    status = models.IntegerField(choices=STATUS, default=0)


    def _str_(self):
        return self.title

class Option(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE,)
    text = models.CharField(max_length=200)

    def _str_(self):
        return self.text

class Response(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    time = models.DateTimeField(db_comment="Date and time when the article was published",)

    def _str_(self):
        return self.name