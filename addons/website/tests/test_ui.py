# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import gerp
import gerp.tests

class TestUiTranslate(gerp.tests.HttpCase):
    def test_admin_tour_rte_translator(self):
        self.phantom_js("/", "gerp.__DEBUG__.services['web_tour.tour'].run('rte_translator')", "gerp.__DEBUG__.services['web_tour.tour'].tours.rte_translator.ready", login='admin', timeout=120)

class TestUi(gerp.tests.HttpCase):
    post_install = True
    at_install = False

    def test_01_public_homepage(self):
        self.phantom_js("/", "console.log('ok')", "'website.content.snippets.animation' in gerp.__DEBUG__.services")

    def test_02_admin_tour_banner(self):
        self.phantom_js("/", "gerp.__DEBUG__.services['web_tour.tour'].run('banner')", "gerp.__DEBUG__.services['web_tour.tour'].tours.banner.ready", login='admin')
