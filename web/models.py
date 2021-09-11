from django.db import models


class Category(models.Model):
    """Model definition for Category."""

    # TODO: Define fields here
    name = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Category."""

        verbose_name = "Category"
        verbose_name_plural = "Category"

    def __str__(self):
        """Unicode representation of Category."""
        return self.name


class Physisian(models.Model):
    """Model definition for Physisian."""

    # TODO: Define fields here
    physisian_code = models.CharField(max_length=11)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    expertise_name = models.CharField(max_length=255)
    mhospital_name = models.CharField(max_length=255)

    class Meta:
        """Meta definition for Physisian."""

        verbose_name = "Physisian"
        verbose_name_plural = "Physisian"

    def __str__(self):
        """Unicode representation of Physisian."""
        return self.first_name + " " + self.last_name


class Patient(models.Model):
    """Model definition for Patient."""

    # TODO: Define fields here
    patient_code = models.CharField(max_length=25)
    patient_name_th = models.CharField(max_length=255)
    patient_name_en = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    physisian = models.ManyToManyField(
        Physisian, default=None, null=True, blank=True)

    class Meta:
        """Meta definition for Patient."""

        verbose_name = "Patient"
        verbose_name_plural = "Patient"

    def __str__(self):
        """Unicode representation of Patient."""
        return self.Patient_name_th
