# -*- coding: UTF-8 -*-
# Django settings for pycon project.
import os
import os.path
import sys

#from django.utils.translation import ugettext as _
_ = lambda x:x

if os.environ.get('DEBUG') == 'True':
    DEBUG = True
else:
    DEBUG = False


TEMPLATE_DEBUG = DEBUG
#DEBUG=True
#APPEND_SLASH=False
ALLOWED_HOSTS = ['*']

ADMINS = (
#    ('alexsavio', 'alexsavio@gmail.com'),
#    ('oiertwo'  , 'badtrex@gmail.com'),
#    ('fpliger'  , 'fabio.pliger@gmail.com'),
#    ('barrachri', 'barrachri@gmail.com'),
#    ('malemburg', 'mal@europython.eu'),
    ('web-wg', 'web-wg@europython.eu'),
)

MANAGERS = ADMINS


ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", '').split(',')
#APPEND_SLASH = False

PROJECT_DIR = os.environ.get('PROJECT_DIR', os.path.normpath(
    os.path.join(os.path.dirname(__file__), '..')))
DATA_DIR = os.environ.get('DATA_DIR', os.path.join(PROJECT_DIR, 'data'))
OTHER_STUFF = os.environ.get('OTHER_STUFF',
                             os.path.join(PROJECT_DIR, 'documents'))

LOGS_DIR = os.path.join(PROJECT_DIR, 'logs/')

if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)

sys.path.insert(0, os.path.join(PROJECT_DIR, 'deps'))

SITE_DATA_ROOT = DATA_DIR + '/site'

DATABASE_TYPE = os.environ.get('DATABASE')

if DATABASE_TYPE == "postgres":
    user = os.environ.get('DATABASE_USER')
    password = os.environ.get('DATABASE_PASSWORD')
    dbname = os.environ.get('DATABASE_NAME')
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': dbname,
        'USER': user,
        'PASSWORD': password,
    }
}
else:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': SITE_DATA_ROOT + '/p3.db',
    }
}

# EuroPython outgoing mail server
EMAIL_HOST = "mail.europython.io"

# Email sender address to use for emails generated by Django for admins
SERVER_EMAIL = 'noreply@europython.eu'

# Email sender address used per default for emails to e.g. attendees
DEFAULT_FROM_EMAIL = 'info@europython.eu'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Madrid'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

# Languages supported by the system, mapping ISO code
# to language. 'en' must always be supported
#
# Note that the system will have to support languages from previous
# conferences as well, so changes have to be applied with care !
#
# TBD: There's another setting called CMS_LANGUAGES. Not sure why we
# need this.
LANGUAGES = (
    ('en', _('English')),
    ('es', _('Spanish')),
    ('eu', _('Basque')),
    ('it', _('Italian')),
)

# These languages are shown in the talk submission forms. The
# tuple must be a subset of LANGUAGES.
CONFERENCE_TALK_SUBMISSION_LANGUAGES = (
    ('en', _('English')),
    ('es', _('Spanish')),
    ('eu', _('Basque')),
)

# Site ID
SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"

MEDIA_ROOT = DATA_DIR + '/media_public'
SECURE_MEDIA_ROOT = DATA_DIR + '/media_private'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'
SECURE_MEDIA_URL = '/p3/secure_media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = DATA_DIR + '/static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key')

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
)

from django.conf import global_settings

#
# XXX THESE SHOULD GO INTO THE OS.ENVIRON !
#
LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get("SOCIAL_AUTH_GOOGLE_OAUTH2_KEY")
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get("SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET")

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.mail.mail_validation',
    'social.pipeline.social_auth.associate_by_email',
    'social.pipeline.user.create_user',
    # THIS IS IMPORTANT!!!! Connect new authenticated users to profiles
    # of the important project apps!!
    'p3.views.profile.connect_profile_to_assopy',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details'
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    'django.contrib.messages.context_processors.messages',
    "django.core.context_processors.i18n",
    "django.core.context_processors.debug",
    "django.core.context_processors.request",
    "django.core.context_processors.media",
    'django.core.context_processors.csrf',
    'django.core.context_processors.request',
    "django.core.context_processors.tz",
    'p3.context_processors.settings',
    'conference.context_processors.current_url',
    'conference.context_processors.stuff',
    "sekizai.context_processors.sekizai",
    "cms.context_processors.cms_settings",
    "django.core.context_processors.static",


   'social.apps.django_app.context_processors.backends',
   'social.apps.django_app.context_processors.login_redirect',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'assopy.middleware.DebugInfo',
    'pycon.middleware.RisingResponse',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

ROOT_URLCONF = 'pycon.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'pycon.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

LOCALE_PATHS = (
    os.path.join(PROJECT_DIR, 'locale'),
)

INSTALLED_APPS = (
    'filebrowser',
    # Warning: the sequence p3/assopy/admin is important to be able to
    # resolve correctly templates

    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'django.contrib.redirects',
    'django.contrib.comments',

    'p3',
    'assopy',
    'assopy.stripe',
    'conference',

    'social.apps.django_app.default',

    'djangocms_text_ckeditor',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_link',
    'cmsplugin_filer_image',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',
    'djangocms_grid',

    'cms',
    'menus',
    'sekizai',
    'tagging',
    'taggit',
    'authority',
    #'pages',
    'mptt',

    'microblog',
    'hcomments',
    'django_xmlrpc',
    'pingback',
    'rosetta',
    'south',
    'email_template',
    'paypal.standard.ipn',
    'filer',
    'easy_thumbnails',

    'captcha',
    'django_crontab',
    'formstyle',

    'cms_migration',
    'markitup',
    'cms_utils',

    'raven.contrib.django.raven_compat',
)

# Google ReCaptcha settings
RECAPTCHA_OPTIONS = {
    'theme': 'clean',
    'lang': 'en',
    'tabindex': 0,
    # 'custom_translations': {},
    #'custom_theme_widget': None
}
RECAPTCHA_PRIVATE_KEY = os.environ.get(
    'RECAPTCHA_PRIVATE_KEY',
    # This needs to be passed in via the OS env:
    'no-private-key-set')
RECAPTCHA_PUBLIC_KEY = os.environ.get(
    'RECAPTCHA_PUBLIC_KEY',
    # Registered for EuroPython domains:
    '6LdFmQcTAAAAAN1xx4M5UN6yg4TwFRXUwIrH5iGh')
RECAPTCHA_USE_SSL = True
NOCAPTCHA = True

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOGS_DIR, 'conference.log'),
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'conference.tags': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': False,
        }
    }
}

AUTHENTICATION_BACKENDS = (
    'assopy.auth_backends.IdBackend',
    'assopy.auth_backends.EmailBackend',
    'assopy.auth_backends.JanRainBackend',
    'django.contrib.auth.backends.ModelBackend',

    'social.backends.facebook.FacebookOAuth2',
   'social.backends.google.GoogleOAuth2',
   'social.backends.twitter.TwitterOAuth',
   # 'django.contrib.auth.backends.ModelBackend',
)


# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/admin/'
FILEBROWSER_URL_FILEBROWSER_MEDIA = '/static/filebrowser/'

PAGE_USE_SITE_ID = False
DEFAULT_PAGE_TEMPLATE = 'cms/content.html'
PAGE_TEMPLATES = (
    # ('cms/index.html', 'homepage'),
    #('cms/index-simple.html', 'homepage (semplificata)'),
    ('cms/p5_homepage.html', 'Homepage'),
    ('cms/content.html', 'Content page'),
    ('cms/content-1col.html', 'Content page, single column'),
    ('cms/p5_home_splash.html', 'Homepage, splash'),
    #('cms/content-assopy.html', 'assopy page (una colonna)'),
)
PAGE_UNIQUE_SLUG_REQUIRED = False
PAGE_TAGGING = True
PAGE_LANGUAGES = (
    ('it-it', _('Italian')),
    ('en-us', _('English')),
)
PAGE_DEFAULT_LANGUAGE = PAGE_LANGUAGES[0][0]
PAGE_LANGUAGE_MAPPING = lambda lang: PAGE_LANGUAGES[0][0]

PAGE_REAL_TIME_SEARCH = False

PAGE_USE_STRICT_URL = True

ROSETTA_EXCLUDED_APPLICATIONS = (
    'debug_toolbar',
    'filebrowser',
    'pages',
    'rosetta',
)

CMS_LANGUAGES = {
    1: [
        {
            'code': 'it',
            'name': _('Italiano'),
        },
        {
            'code': 'en',
            'name': _('English'),
        },
    ],
    'default': {
        'fallbacks': ['en', 'it'],
        'redirect_on_fallback': True,
        'public': True,
        'hide_untranslated': False,

    }
}
CMS_TEMPLATES = (
    ('django_cms/p5_homepage.html', 'Homepage'),
    ('django_cms/content.html', 'Content page'),
    ('django_cms/content-1col.html', 'Content page, single column'),
    ('django_cms/p5_home_splash.html', 'Homepage, splash'),
)
CMS_PLUGIN_PROCESSORS = (
    'cms_utils.processors.process_templatetags',
)
MARKITUP_FILTER = ('markdown2.markdown', {'safe_mode': False})

CKEDITOR_SETTINGS = {
    'height': 300,
    'stylesSet': 'default:/static/p6/javascripts/ckeditor.wysiwyg.js',
    'contentsCss': ['/static/css/base.css'],
    'language': '{{ language }}',
    'toolbar': 'CMS',
    'skin': 'moono',
    'extraPlugins': 'cmsplugins',
}


#
# We're not going to use this feature for EuroPython 2015+:
#
MICROBLOG_LINK = 'http://blog.europython.eu'
MICROBLOG_TITLE = 'EuroPython Blog'
MICROBLOG_DESCRIPTION = 'Latest news from EuroPython'
MICROBLOG_DEFAULT_LANGUAGE = 'en'
MICROBLOG_POST_LIST_PAGINATION = True
MICROBLOG_POST_PER_PAGE = 10
MICROBLOG_MODERATION_TYPE = 'akismet'
MICROBLOG_AKISMET_KEY = '56c34997206c'
MICROBLOG_EMAIL_RECIPIENTS = ['pycon-organization@googlegroups.com']
MICROBLOG_EMAIL_INTEGRATION = True

MICROBLOG_TWITTER_USERNAME = 'europython'
MICROBLOG_TWITTER_POST_URL_MANGLER = 'microblog.utils.bitly_url'
MICROBLOG_TWITTER_INTEGRATION = False

MICROBLOG_PINGBACK_SERVER = False
MICROBLOG_TRACKBACK_SERVER = False

SOUTH_MIGRATION_MODULES = {
    'easy_thumbnails': 'easy_thumbnails.south_migrations',
}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)
THUMBNAIL_HIGH_RESOLUTION = True

DJANGOCMS_GRID_CONFIG = {
    'COLUMNS': 100,
    'TOTAL_WIDTH': 960,
    'GUTTER': 20,
}


def MICROBLOG_POST_FILTER(posts, user):
    if user and user.is_staff:
        return posts
    else:
        return filter(lambda x: x.is_published(), posts)


SESSION_COOKIE_NAME = 'p5_sessionid'

#
# XXX THESE NEED TO GO INTO OS.ENVIRON !!!
#
CONFERENCE_OLARK_KEY = '1751-12112149-10-1389'
CONFERENCE_GOOGLE_MAPS = {
    # chiave info@europython.eu per http://localhost
    # 'key': 'ABQIAAAAaqki7uO3Z2gFXuaDbZ-9BBT2yXp_ZAY8_ufC3CFXhHIE1NvwkxSCRpOQNQwH5i15toJmp6eLWzSKPg',
    # chiave info@europython.eu per http://europython.eu
    'key': 'ABQIAAAAaqki7uO3Z2gFXuaDbZ-9BBT8rJViP5Kd0PVV0lwN5R_47a678xQFxoY_vNcqiT-2xRPjGe6Ua3A5oQ',
    'country': 'es',
}

CONFERENCE_CONFERENCE = 'ep2016'
CONFERENCE_SEND_EMAIL_TO = [ 'helpdesk@europython.eu', ]
CONFERENCE_TALK_SUBMISSION_NOTIFICATION_EMAIL = []
CONFERENCE_VOTING_DISALLOWED = 'https://ep2016.europython.eu/en/talk-voting/'

CONFERENCE_FORMS = {
    'PaperSubmission': 'p3.forms.P3SubmissionForm',
    'AdditionalPaperSubmission': 'p3.forms.P3SubmissionAdditionalForm',
    'Profile': 'p3.forms.P3ProfileForm',
    'EventBooking': 'p3.forms.P3EventBookingForm',
}

CONFERENCE_TALKS_RANKING_FILE = SITE_DATA_ROOT + '/rankings.txt'
CONFERENCE_ADMIN_TICKETS_STATS_EMAIL_LOG = SITE_DATA_ROOT + '/admin_ticket_emails.txt'
CONFERENCE_ADMIN_TICKETS_STATS_EMAIL_LOAD_LIBRARY = ['p3', 'conference']

# Conference sub-communities
CONFERENCE_TALK_SUBCOMMUNITY = (
    ('', _('All')),
    ('pydata', _('PyData')),
)

### Ticket information

# T-shirt sizes
CONFERENCE_TICKET_CONFERENCE_SHIRT_SIZES = (
    ('fs', 'S (female)'),
    ('fm', 'M (female)'),
    ('fl', 'L (female)'),
    ('fxl', 'XL (female)'),
    ('fxxl', 'XXL (female)'),
    ('fxxxl', '3XL (female)'),
    ('s', 'S (male)'),
    ('m', 'M (male)'),
    ('l', 'L (male)'),
    ('xl', 'XL (male)'),
    ('xxl', 'XXL (male)'),
    ('xxxl', '3XL (male)'),
    ('xxxxl', '4XL (male)'),
)

# Available diets
CONFERENCE_TICKET_CONFERENCE_DIETS = (
    ('omnivorous', _('Omnivorous')),
    ('vegetarian', _('Vegetarian')),
    #('vegan', _('Vegan')),
    #('kosher', _('Kosher')),
    ('other', _('Other')),
)

# Python experience
CONFERENCE_TICKET_CONFERENCE_EXPERIENCES = (
    (0, _('no comment')),
    (1, _('1 star  (just starting)')),
    (2, _('2 stars (beginner)')),
    (3, _('3 stars (intermediate)')),
    (4, _('4 stars (expert))')),
    (5, _('5 stars (guru level)')),
)


def CONFERENCE_TICKETS(conf, ticket_type=None, fare_code=None):
    from p3 import models

    tickets = models.Ticket.objects \
        .filter(fare__conference=conf, orderitem__order___complete=True)
    if ticket_type:
        tickets = tickets.filter(fare__ticket_type=ticket_type)
    if fare_code:
        if fare_code.endswith('%'):
            tickets = tickets.filter(fare__code__startswith=fare_code[:-1])
        else:
            tickets = tickets.filter(fare__code=fare_code)
    return tickets


def CONFERENCE_VOTING_OPENED(conf, user):
    # Can access the page:
    #   anyone during community voting
    #   superusers
    #   speakers (of current conference)
    #   who is in the special "pre_voting" group
    if user.is_superuser:
        return True

    # Only allow access during talk voting period
    if conf.voting():
        return True
    else:
        return False

    # XXX Disabled these special cases, since it's not clear
    #     what they are used for
    if 0:
        from p3.models import TalkSpeaker, Speaker
        try:
            count = TalkSpeaker.objects.filter(
                talk__conference=CONFERENCE_CONFERENCE,
                speaker=user.speaker).count()
        except (AttributeError, Speaker.DoesNotExist):
            pass
        else:
            if count > 0:
                return True

        # Special case for "pre_voting" group members;
        if user.groups.filter(name='pre_voting').exists():
            return True

    return False

def CONFERENCE_VOTING_ALLOWED(user):

    """ Determine whether user is allowed to participate in talk voting.

    """
    if not user.is_authenticated():
        return False
    if user.is_superuser:
        return True

    # Speakers of the current conference are always allowed to vote
    from p3.models import TalkSpeaker, Speaker
    try:
        count = TalkSpeaker.objects.filter(
            talk__conference=CONFERENCE_CONFERENCE,
            speaker=user.speaker).count()
    except Speaker.DoesNotExist:
        pass
    else:
        if count > 0:
            return True

    # People who have a ticket for the current conference assigned to
    # them can vote
    from p3 import models
    # Starting with EP2016, we know that all assigned tickets have
    # .assigned_to set correctly
    tickets = models.TicketConference.objects \
              .filter(ticket__fare__conference=CONFERENCE_CONFERENCE,
                      assigned_to=user.email)

    # Old query:
    #from django.db.models import Q
    # tickets = models.TicketConference.objects \
    #     .available(user, CONFERENCE_CONFERENCE) \
    #     .filter(Q(orderitem__order___complete=True) | Q(
    #     orderitem__order__method='admin')) \
    #     .filter(Q(p3_conference=None) | Q(p3_conference__assigned_to='') | Q(
    #     p3_conference__assigned_to=user.email))
    return tickets.count() > 0


def CONFERENCE_SCHEDULE_ATTENDEES(schedule, forecast):
    from p3.stats import presence_days
    from conference.models import Schedule

    if not isinstance(schedule, Schedule):
        output = {}
        for s in Schedule.objects.filter(conference=schedule):
            output[s.id] = CONFERENCE_SCHEDULE_ATTENDEES(s, forecast)
        return output
    d = schedule.date.strftime('%Y-%m-%d')
    s = presence_days(schedule.conference)
    for row in s['data']:
        if row['title'] == '%s (no staff)' % d:
            if forecast:
                return row['total_nc']
            else:
                return row['total']
    return 0


CONFERENCE_ADMIN_ATTENDEE_STATS = (
    'p3.stats.tickets_status',
    'p3.stats.hotel_tickets',
    'p3.stats.conference_speakers',
    'p3.stats.conference_speakers_day',
    'p3.stats.speaker_status',
    'p3.stats.presence_days',
    'p3.stats.shirt_sizes',
    'p3.stats.diet_types',
    'p3.stats.pp_tickets',
)


def CONFERENCE_VIDEO_COVER_EVENTS(conference):
    from p3 import dataaccess
    from p3 import models
    from datetime import timedelta

    conf = models.Conference.objects.get(code=conference)

    def valid(e):
        if e['tags'] & set(['special', 'break']):
            return False
        # sprints are in the last two days
        if e['time'].date() >= conf.conference_end - timedelta(days=1):
            return False
        # evening events are not recorded
        if e['time'].hour >= 20:
            return False
        if len(e['tracks']) == 1 and (
            e['tracks'][0] in ('helpdesk1', 'helpdesk2')):
            return False
        return True

    return [x['id'] for x in filter(valid, dataaccess.events(conf=conference))]


def CONFERENCE_VIDEO_COVER_IMAGE(eid, type='front', thumb=False):
    import re
    import os.path
    from PIL import Image, ImageDraw, ImageFont
    from p3 import dataaccess

    event = dataaccess.event_data(eid)
    conference = event['conference']

    stuff = os.path.normpath(
        os.path.join(os.path.dirname(__file__), '..', 'documents', 'cover',
                     conference))
    if not os.path.isdir(stuff):
        return None

    def wrap_text(font, text, width):
        words = re.split(' ', text)
        lines = []
        while words:
            word = words.pop(0).strip()
            if not word:
                continue
            if not lines:
                lines.append(word)
            else:
                line = lines[-1]
                w, h = font.getsize(line + ' ' + word)
                if w <= width:
                    lines[-1] += ' ' + word
                else:
                    lines.append(word)

        for ix, line in enumerate(lines):
            line = line.strip()
            while True:
                w, h = font.getsize(line)
                if w <= width:
                    break
                line = line[:-1]
            lines[ix] = line
        return lines

    if conference in ('ep2012', 'ep2013', 'ep2015', 'ep2016'):
        master = Image.open(os.path.join(stuff, 'cover-start-end.png')).convert(
            'RGBA')

        if type == 'back':
            return master

        if conference == 'ep2012':
            ftitle = ImageFont.truetype(
                os.path.join(stuff, 'League Gothic.otf'),
                36, encoding="unic")
            fauthor = ImageFont.truetype(
                os.path.join(stuff, 'Arial_Unicode.ttf'),
                21, encoding="unic")
            y = 175
        elif conference in ('ep2013', 'ep2015', 'ep2016'):
            ftitle = ImageFont.truetype(
                os.path.join(stuff, 'League_Gothic.otf'),
                36, encoding="unic")
            fauthor = ImageFont.truetype(
                os.path.join(stuff, 'League_Gothic.otf'),
                28, encoding="unic")
            y = 190

        width = master.size[0] - 40
        d = ImageDraw.Draw(master)

        title = event['name']
        if event.get('custom'):
            # this is a custom event, if starts with an anchor we can
            # extract the reference
            m = re.match(r'<a href="(.*)">(.*)</a>', title)
            if m:
                title = m.group(2)
        lines = wrap_text(ftitle, title, width)
        for l in lines:
            d.text((20, y), l, font=ftitle, fill=(0x2f, 0x1c, 0x1c, 0xff))
            y += ftitle.getsize(l)[1] + 8

        if event.get('talk'):
            spks = [x['name'] for x in event['talk']['speakers']]
            text = 'by ' + ','.join(spks)
            lines = wrap_text(fauthor, text, width)
            for l in lines:
                d.text((20, y), l, font=fauthor, fill=(0x3d, 0x7e, 0x8a, 0xff))
                y += fauthor.getsize(l)[1] + 8

        if thumb:
            master.thumbnail(thumb, Image.ANTIALIAS)
        return master
    else:
        return None


CONFERENCE_TICKET_BADGE_ENABLED = True
CONFERENCE_TICKET_BADGE_PROG_ARGS = ['-e', '0', '-p', 'A4', '-n', '1']


def CONFERENCE_TICKET_BADGE_PREPARE_FUNCTION(tickets):
    from p3.utils import conference_ticket_badge

    return conference_ticket_badge(tickets)


def CONFERENCE_TALK_VIDEO_ACCESS(request, talk):
    return True
    if talk.conference != CONFERENCE_CONFERENCE:
        return True
    u = request.user
    if u.is_anonymous():
        return False
    from p3.models import Ticket

    qs = Ticket.objects \
        .filter(id__in=[x.id for x in u.assopy_user.tickets()]) \
        .filter(orderitem__order___complete=True,
                fare__ticket_type='conference')
    return qs.exists()


def ASSOPY_ORDERITEM_CAN_BE_REFUNDED(user, item):
    if user.is_superuser:
        return True
    return False
    if not item.ticket:
        return False
    ticket = item.ticket
    if ticket.user != user:
        return False
    if ticket.fare.conference != CONFERENCE_CONFERENCE:
        return False
    if item.order.total() == 0:
        return False
    return item.order._complete


#
# XXX What is this AssoPy stuff ?
#
GENRO_BACKEND = False
ASSOPY_VIES_WSDL_URL = None
ASSOPY_BACKEND = 'https://assopy.europython.eu/conference/externalcall'
ASSOPY_SEARCH_MISSING_USERS_ON_BACKEND = False
ASSOPY_TICKET_PAGE = 'p3-tickets'
ASSOPY_SEND_EMAIL_TO = ['billing-log@europython.io']
ASSOPY_REFUND_EMAIL_ADDRESS = {
    'approve': ['info@europython.eu'],
    'execute': {
        None: ['dvd@gnx.it'],
        'bank': ['matteo@europython.eu'],
    },
    'credit-note': ['michele.bertoldi@gmail.com'],
}

ASSOPY_OTC_CODE_HANDLERS = {
    'e': 'p3.views.OTCHandler_E',
}

#
# This URL needs to be set to the main URL of the site.
#
# It is used for generating URLs pointing back to the site
# in quite a few places.
#
DEFAULT_URL_PREFIX = 'https://ep2016.europython.eu'

PINGBACK_TARGET_DOMAIN = 'ep2016.europython.eu'
COMMENTS_APP = 'hcomments'

P3_FARES_ENABLED = lambda u: True

# Disabled until we find out how to use europython-announce for this:
#P3_NEWSLETTER_SUBSCRIBE_URL = "https://mail.python.org/mailman/subscribe/europython-announce"
P3_NEWSLETTER_SUBSCRIBE_URL = ""

P3_TWITTER_USER = MICROBLOG_TWITTER_USERNAME
P3_USER_MESSAGE_FOOTER = '''

This message was sent from a participant at the EuroPython conference.
Your email address is not disclosed to anyone, to stop receiving messages
from other users you can change your privacy settings from this page:
https://ep2016.europython.eu/accounts/profile/
'''

HAYSTACK_SITECONF = 'web_site.search_sites'
HAYSTACK_SEARCH_ENGINE = 'whoosh'


def HCOMMENTS_RECAPTCHA(request):
    return not request.user.is_authenticated()


def HCOMMENTS_THREAD_OWNERS(o):
    from p3.models import P3Talk
    from microblog.models import Post

    if isinstance(o, P3Talk):
        return [s.user for s in o.get_all_speakers()]
    elif isinstance(o, Post):
        return [o.author, ]
        return [o.author, ]
    return None


def HCOMMENTS_MODERATOR_REQUEST(request, comment):
    if request.user.is_superuser:
        return True
    else:
        owners = HCOMMENTS_THREAD_OWNERS(comment.content_object)
        if owners:
            return request.user in owners
    return False


P3_ANONYMOUS_AVATAR = 'p5/images/headshot-default.jpg'

P3_LIVE_INTERNAL_IPS = ('2.228.78.', '10.3.3.', '127.0.0.1')
P3_INTERNAL_SERVER = 'live.ep:1935'

P3_LIVE_TRACKS = {
    'track1': {
        'stream': {
            'external': 'WQnU7Qvy-xg',
            'internal': 'live/spaghetti',
        }
    },
    'track2': {
        'stream': {
            'external': 'urwOdSH3Tyg',
            'internal': 'live/lasagne',
        }
    },
    'track3': {
        'stream': {
            'external': 'tdGKPPlhqAI',
            'internal': 'live/ravioli',
        }
    },
    'track4': {
        'stream': {
            'external': 'IeKx5Qy_8lY',
            'internal': 'live/tagliatelle',
        }
    },
    'track-ita': {
        'stream': {
            'external': 'JSjXKGom9VI',
            'internal': 'live/bigmac',
        }
    },
    'training1': {
        'stream': {
            'external': '6CG-25uxPdI',
            'internal': 'live/pizzamargherita',
        }
    },
    'training2': {
        'stream': {
            'external': 'iy1phHF-mec',
            'internal': 'live/pizzanapoli',
        }
    },
}


def P3_LIVE_REDIRECT_URL(request, track):
    internal = False
    for check in P3_LIVE_INTERNAL_IPS:
        if request.META['REMOTE_ADDR'].startswith(check):
            internal = True
            break
    url = None
    if internal:
        import re

        ua = request.META['HTTP_USER_AGENT']

        base = '{0}/{1}'.format(P3_INTERNAL_SERVER,
                                P3_LIVE_TRACKS[track]['stream']['internal'])
        if re.search('Android', ua, re.I):
            url = 'rtsp://' + base
        elif re.search('iPhone|iPad|iPod', ua, re.I):
            url = 'http://%s/playlist.m3u8' % base
        else:
            url = 'rtmp://' + base
    else:
        try:
            url = 'https://www.youtube.com/watch?v={0}'.format(
                P3_LIVE_TRACKS[track]['stream']['external'])
        except KeyError:
            pass
    return url


def P3_LIVE_EMBED(request, track=None, event=None):
    from django.core.cache import cache

    if not any((track, event)) or all((track, event)):
        raise ValueError('track or event, not both')

    if event:
        # ep2012, all keynotes are recorded in track "lasagne"
        if 'keynote' in event['tags'] or len(event['tracks']) > 1:
            track = 'track2'
        else:
            track = event['tracks'][0]

    internal = False
    for check in P3_LIVE_INTERNAL_IPS:
        if request.META['REMOTE_ADDR'].startswith(check):
            internal = True
            break

    if internal:
        try:
            url = '{0}/{1}'.format(P3_INTERNAL_SERVER,
                                   P3_LIVE_TRACKS[track]['stream']['internal'])
        except KeyError:
            return None
        data = {
            'track': track,
            'stream': url.rsplit('/', 1)[1],
            'url': url,
        }
        html = ("""
        <div>
            <div class="button" style="float: left; margin-right: 20px;">
                <h5><a href="rtsp://%(url)s">RTSP</a></h5>
                For almost all<br/>Linux, Windows, Android
            </div>
            <div class="button" style="float: left; margin-right: 20px;">
                <h5><a href="http://%(url)s/playlist.m3u8">HLS&#xF8FF;</a></h5>
                Apple world (mainly)
            </div>
            <div class="button" style="float: left; margin-right: 20px;">
                <h5><a href="#" onclick="start_%(stream)s(); return false;">Flash</a></h5>
                Old good school
            </div>
            <div id="stream-%(track)s" style="clear: both();width:530px;height:298px;margin:0 auto;text-align:center"> </div>
            <script>
                function start_%(stream)s() {
                    $f("stream-%(track)s", "/static/p5/flowplayer/flowplayer-3.2.12.swf", {

                        clip: {
                            autoPlay: false,
                            url: 'mp4:%(stream)s',
                            scaling: 'fit',
                            // configure clip to use hddn as our provider, refering to our rtmp plugin
                            provider: 'hddn'
                        },

                        // streaming plugins are configured under the plugins node
                        plugins: {

                            // here is our rtmp plugin configuration
                            hddn: {
                                url: "/static/p5/flowplayer/flowplayer.rtmp-3.2.10.swf",

                                // netConnectionUrl defines where the streams are found
                                netConnectionUrl: 'rtmp://%(url)s'
                            }
                        }
                    });
                }
            </script>
        </div>
        """ % data) #" (makes emacs highlighting happy)
        return html
    else:
        data = cache.get('p3_live_embed_%s' % track)
        if data is not None:
            return data

        try:
            yurl = 'https://www.youtube.com/watch?v={0}'.format(
                P3_LIVE_TRACKS[track]['stream']['external'])
        except KeyError:
            return None

        import httplib2, json

        http = httplib2.Http()
        service = 'https://www.youtube.com/oembed'
        url = service + '?url=' + yurl + '&format=json&scheme=https'
        try:
            response, content = http.request(url)
            data = json.loads(content)
        except:
            return None
        cache.set('p3_live_embed_%s' % track, data['html'], 3600)
        return data['html']


# cronjob

def cron_cleanup():
    from django.core.management.commands import cleanup

    cmd = cleanup.Command()
    cmd.handle()


CRONTAB_COMMAND_PREFIX = 'DATA_DIR=%s OTHER_STUFF=%s' % (DATA_DIR, OTHER_STUFF)
CRONJOBS = [
    ('@weekly', 'pycon.settings.cron_cleanup')
]

STRIPE_ENABLED = True
STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY")
STRIPE_PUBLISHABLE_KEY = os.environ.get("STRIPE_PUBLISHABLE_KEY")
STRIPE_COMPANY_NAME = os.environ.get("STRIPE_COMPANY_NAME")
STRIPE_COMPANY_LOGO = os.environ.get("STRIPE_COMPANY_LOGO")
STRIPE_CURRENCY = "EUR"
STRIPE_ALLOW_REMEMBER_ME = False


# Put your google maps key here
CONFERENCE_GOOGLE_MAPS = {
    'key': '',
    'country': 'es',
}



# Paypal merchant email
PAYPAL_RECEIVER_EMAIL = os.environ.get("PAYPAL_RECEIVER_EMAIL")

# If the merchant account is a debug one set this flag to True
if os.environ.get('PAYPAL_TEST') == 'False':
    PAYPAL_TEST = False
else:
    PAYPAL_TEST = True

# Janrain account
ASSOPY_JANRAIN = {
    'domain': '',
    'app_id': '',
    'secret': '',
}

# Sentry account
RAVEN_CONFIG = {
    'dsn': '',
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# MAL 2015-03-03: We need the emails going out rather than to the
# console, so commenting this out for now.
#if DEBUG:
#    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

if DEBUG:
    LOGGING['loggers']['django.request']['handlers'].append('console')
# files under SECURE_MEDIA_BOOT must be served by django, this if
# is needed to avoid they end up in a subdir of MEDIA_ROOT that is
# normally served by an external webserver
import os.path

check = os.path.commonprefix((MEDIA_ROOT, SECURE_MEDIA_ROOT))
if check.startswith(MEDIA_ROOT):
    if not DEBUG:
        raise RuntimeError('SECURE_MEDIA_ROOT cannot be a subdir of MEDIA_ROOT')
    else:
        print
        'WARN, SECURE_MEDIA_ROOT is a subdir of MEDIA_ROOT'

from django.core.files import storage

SECURE_STORAGE = storage.FileSystemStorage(location=SECURE_MEDIA_ROOT,
                                           base_url=SECURE_MEDIA_URL)

if not SECRET_KEY:
    if not DEBUG:
        raise RuntimeError('SECRET_KEY not set')
    else:
        print
        'WARN, SECRET_KEY not set'


### Override any settings with local settings

try:
    from pycon.settings_locale import *
except ImportError, reason:
    #import sys
    #sys.stderr.write('Could not import local settings: %s\n' % reason)
    pass
