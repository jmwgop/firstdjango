from django.db import models

class DocumentIndex(models.Model):
    did = models.AutoField(max_length=20, primary_key=True)
    doc_type = models.CharField(50)
    eff_date = models.DateField()
    file_date = models.DateField()
    volume = models.CharField(4)
    page = models.CharField(4)
    rec_type = models.CharField(2)
    year = models.CharField(4)
    doc_num = models.CharField(20)

    def __str__(self):
        return '%s %s %s %s %s %s %s %s' % (self.doc_type, self.eff_date, self.file_date, self.volume, self.page, self.rec_type, self.year, self.doc_num)

class GrantorIndex(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    did = models.ForeignKey('DocumentIndex', on_delete=models.CASCADE)
    grantor = models.TextField()

    def __str__(self):
        return self.grantor

class GranteeIndex(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    did = models.ForeignKey('DocumentIndex', on_delete=models.CASCADE)
    grantee = models.TextField()

    def __str__(self):
        return self.grantee

class ImageIndex(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    did = models.ForeignKey('DocumentIndex', on_delete=models.CASCADE)
    img_pg = models.TextField()

    def __str__(self):
        return self.img_pg

class LegalIndex(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    did = models.ForeignKey('DocumentIndex', on_delete=models.CASCADE)
    legal = models.TextField()

    def __str__(self):
        return self.legal

class DocumentIndex(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    did = models.ForeignKey('DocumentIndex', on_delete=models.CASCADE)
    grantor = models.ForeignKey('GrantorIndex', on_delete=models.CASCADE)
    grantee = models.ForeignKey('GranteeIndex', on_delete=models.CASCADE)
    doc_type = models.ForeignKey('DocumentIndex', on_delete=models.CASCADE)
    eff_date = models.ForeignKey('DocumentIndex', on_delete=models.CASCADE)
    file_date = models.ForeignKey('DocumentIndex', on_delete=models.CASCADE)
    volume = models.ForeignKey('DocumentIndex', on_delete=models.CASCADE)
    page = models.ForeignKey('DocumentIndex', on_delete=models.CASCADE)
    rec_type = models.ForeignKey('DocumentIndex', on_delete=models.CASCADE)
    year = models.ForeignKey('DocumentIndex', on_delete=models.CASCADE)
    doc_num = models.ForeignKey('DocumentIndex', on_delete=models.CASCADE)
    legal = models.ForeignKey('LegalIndex', on_delete=models.CASCADE)
    img_pages = models.ForeignKey('ImageIndex', on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s %s %s %s %s %s' % (self.grantor, self.grantee, self.doc_type, self.eff_date, self.file_date, self.volume, self.page, self.rec_type, self.year, self.doc_num, self.legal, self.img_pages)

# class RunsheetRequests(models.Model):
#     id = models.CharField(max_length=20, primary_key=True)
#     landman = models.CharField()
#     broker = models.CharField()
#     section = models.CharField()
#     subdivision = models.CharField()
#     block = models.CharField()
#     lot = models.CharField()
#     doc_count = models.IntegerField()
#     created_at = models.DateTimeField()
#     document_list =
