# Copyright 2012 Rooter Analysis S.L.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import uuid

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
from django.utils.translation import ugettext_lazy as _

from adminsortable.models import Sortable


class UserApi(Sortable):

    user = models.ForeignKey(User, verbose_name=_(u'User'),
                             blank=False, null=False, unique=True)
    key = models.CharField(verbose_name=_(u'Key'), max_length=40, blank=False,
                           null=False, unique=True, help_text=_(u'Will be autogenerated'))

    class Meta(Sortable.Meta):
        verbose_name = _(u'User Api')
        verbose_name_plural = _(u'User Apis')

    def __unicode__(self):
        return "Apikey of %s  :::  %s" % (self.user.username, str(self.key))


def pre_save_userapi(sender, **kwargs):
    userapi = kwargs['instance']
    if not userapi.key:
        userapi.key = unicode(uuid.uuid4())

pre_save.connect(pre_save_userapi, sender=UserApi)
