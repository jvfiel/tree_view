# -*- coding: utf-8 -*-
# Copyright (c) 2015, MN Tech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils.nestedset import NestedSet
from frappe.model.naming import make_autoname,set_new_name

class Tree(NestedSet):
    nsm_parent_field = 'parent_tree'
    def autoname(self):
        if self.attachment:
            filename = ''
            rev_series = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                          'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

            count_item = frappe.db.sql("""SELECT Count(*) FROM `tabTree` where item='{0}'""".format(self.item))
            print "######################"
            print count_item
            if count_item[0][0] == 0:
                filename = self.item + ' ' + 'Rev. A'
            elif count_item[0][0] > 0:
                filename = self.item + ' ' + 'Rev. ' + rev_series[count_item[0][0]]

            #x = """Update `tabTree` set name = '{0}' where item = '{1}' and name='{2}'""" \
            #    .format(filename, self.item, self.name)
            #print x
            #frappe.db.sql(x)
            #print filename
            self.name = filename

    def validate(self):
        print "````````````````````"
        print "RENAMING..."
        filename = ''
        rev_series = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                      'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        if self.attachment:
            count_item = frappe.db.sql("""SELECT name FROM `tabTree` where item='{0}'""".format(self.item))
            print "######################"
            print count_item
            if not count_item: #FIRST
                filename = self.item + ' ' + 'Rev. A [ACTIVE]'
            else:
                filename = self.item + ' ' + 'Rev. ' + rev_series[len(count_item)] + ' [ACTIVE]'
                # RENAME PREVIOUS FILES FROM ACTIVE TO ARCHIVE
                for item in count_item:
                    print "ARCHIVING..."
                    archive_name = item[0].replace('[ACTIVE]','[ARCHIVE]')
                    archive_sql = """Update `tabTree` set name = '{0}' where name='{1}'""".format(archive_name, item[0])
                    print archive_sql
                    frappe.db.sql(archive_sql)
                    print "`````````````````"

            x = """Update `tabTree` set name = '{0}' where item = '{1}' and name='{2}'""" \
                .format(filename, self.item, self.name)
            print x
            #frappe.db.sql(x)
            #frappe.db.commit()
            print filename
            self.new_name = filename
            #self.name = make_autoname(filename)
            #set_new_name(self)



def rename(doc,method):
    print "````````````````````"
    print "RENAMING..."
    filename = ''
    rev_series = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                  'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    if doc.attachment:
        count_item = frappe.db.sql("""SELECT Count(*) FROM `tabTree` where item='{0}'""".format(doc.item))
        print "######################"
        print count_item
        if count_item[0][0] == 0:
            filename = doc.item + ' ' + 'Rev. A'
        elif count_item[0][0] > 0:
            filename = doc.item + ' ' + 'Rev. ' + rev_series[count_item[0][0]]

        x = """Update `tabTree` set name = '{0}' where item = '{1}' and name='{2}'""" \
            .format(filename, doc.item, doc.name)
        print x
        frappe.db.sql(x)
