from django.db import models


class Category(models.Model):
    """Model definition for Hospital."""

    # TODO: Define fields here
    name = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Hospital."""

        verbose_name = "Hospital"
        verbose_name_plural = "Hospital"

    def __str__(self):
        """Unicode representation of Hospital."""
        return self.name


class Student(models.Model):
    """Model definition for Physisian."""

    # TODO: Define fields here
    student_code = models.CharField(max_length=11)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        """Meta definition for Physisian."""

        verbose_name = "Physisian"
        verbose_name_plural = "Physisians"

    def __str__(self):
        """Unicode representation of Physisian."""
        return self.first_name + " " + self.last_name


class Subject(models.Model):
    """Model definition for Patient."""

    # TODO: Define fields here
    subject_code = models.CharField(max_length=25)
    subject_name_th = models.CharField(max_length=255)
    subject_name_en = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    student = models.ManyToManyField(
        Student, default=None, null=True, blank=True)

    class Meta:
        """Meta definition for Patient."""

        verbose_name = "Patient"
        verbose_name_plural = "Patient"

    def __str__(self):
        """Unicode representation of Patient."""
        return self.subject_name_th
