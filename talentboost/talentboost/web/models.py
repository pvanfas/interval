from django.db import models


class Achievement(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="achievements/")

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="news/")
    date = models.DateField()
    content = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "News"

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="projects/")
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Feature(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="featured/")
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Winner(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="winners/")

    def __str__(self):
        return self.title


class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()

    def __str__(self):
        return self.question


class Setting(models.Model):
    video_id = models.CharField(max_length=11)
    instagram_url = models.URLField()
    youtube_url = models.URLField()
    whatsapp_url = models.URLField()
    website_url = models.URLField()

    def __str__(self):
        return "Change Settings"

    class Meta:
        verbose_name = "Change Settings"
        verbose_name_plural = "Change Settings"
