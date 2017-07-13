# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
import csv
from app.models import *
from django.contrib.auth.models import User
from datetime import datetime

class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('export_facturier.csv', 'rb') as f:
            reader = csv.reader(f, delimiter=';', quotechar='|')
            reader.next()
            check_list = []
            projid = 0
            for row in reader:
                id, customer, status, creation_date, update_date, product, price, qty = row

                if id not in check_list:
                    check_list.append(id)

                    proj = Project(id_user=User.objects.get(id=1),
                                    id_client= Client.objects.get(id=1),)

                    desc = id[:2]

                    if desc == "DV" and status == "STANDBY":
                        proj.status = "Devis en Cours"
                    elif desc == "DV" and status == "LOST":
                        proj.status = "Devis Perdu"
                        if update_date:
                            proj.date_refusal = datetime.strptime(update_date, "%d/%m/%y %H:%M")
                    elif desc == "FA" and status == "STANDBY":
                        proj.status = "Facture en Cours"
                        if update_date:
                            proj.date_acceptance = datetime.strptime(update_date, "%d/%m/%y %H:%M")
                    elif desc == "FA" and status == "PAID":
                        proj.status = "Facture Payée"
                        if update_date:
                            proj.date_payment = datetime.strptime(update_date, "%d/%m/%y %H:%M")

                    proj.creation_date = datetime.strptime(creation_date, "%d/%m/%y %H:%M")
                    proj.name = product
                    proj.save()

                    projid = proj.id

                    line = Project_line(id_project=Project.objects.get(id=projid))
                    line.name = product
                    line.quantity = qty
                    line.unit_price = price

                    line.save()

                else :
                    line = Project_line(id_project=Project.objects.get(id=projid))
                    line.name = product
                    line.quantity = qty
                    line.unit_price = price

                    line.save()
