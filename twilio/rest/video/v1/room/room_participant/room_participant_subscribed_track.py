# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class SubscribedTrackList(ListResource):
    """  """

    def __init__(self, version, room_sid, subscriber_sid):
        """
        Initialize the SubscribedTrackList

        :param Version version: Version that contains the resource
        :param room_sid: The room_sid
        :param subscriber_sid: The subscriber_sid

        :returns: twilio.rest.video.v1.room.room_participant.room_participant_subscribed_track.SubscribedTrackList
        :rtype: twilio.rest.video.v1.room.room_participant.room_participant_subscribed_track.SubscribedTrackList
        """
        super(SubscribedTrackList, self).__init__(version)

        # Path Solution
        self._solution = {'room_sid': room_sid, 'subscriber_sid': subscriber_sid, }
        self._uri = '/Rooms/{room_sid}/Participants/{subscriber_sid}/SubscribedTracks'.format(**self._solution)

    def stream(self, date_created_after=values.unset,
               date_created_before=values.unset, track=values.unset,
               publisher=values.unset, kind=values.unset, limit=None,
               page_size=None):
        """
        Streams SubscribedTrackInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param datetime date_created_after: The date_created_after
        :param datetime date_created_before: The date_created_before
        :param unicode track: The track
        :param unicode publisher: The publisher
        :param SubscribedTrackInstance.Kind kind: The kind
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.video.v1.room.room_participant.room_participant_subscribed_track.SubscribedTrackInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            track=track,
            publisher=publisher,
            kind=kind,
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, date_created_after=values.unset,
             date_created_before=values.unset, track=values.unset,
             publisher=values.unset, kind=values.unset, limit=None, page_size=None):
        """
        Lists SubscribedTrackInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param datetime date_created_after: The date_created_after
        :param datetime date_created_before: The date_created_before
        :param unicode track: The track
        :param unicode publisher: The publisher
        :param SubscribedTrackInstance.Kind kind: The kind
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.video.v1.room.room_participant.room_participant_subscribed_track.SubscribedTrackInstance]
        """
        return list(self.stream(
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            track=track,
            publisher=publisher,
            kind=kind,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, date_created_after=values.unset,
             date_created_before=values.unset, track=values.unset,
             publisher=values.unset, kind=values.unset, page_token=values.unset,
             page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of SubscribedTrackInstance records from the API.
        Request is executed immediately

        :param datetime date_created_after: The date_created_after
        :param datetime date_created_before: The date_created_before
        :param unicode track: The track
        :param unicode publisher: The publisher
        :param SubscribedTrackInstance.Kind kind: The kind
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SubscribedTrackInstance
        :rtype: twilio.rest.video.v1.room.room_participant.room_participant_subscribed_track.SubscribedTrackPage
        """
        params = values.of({
            'DateCreatedAfter': serialize.iso8601_datetime(date_created_after),
            'DateCreatedBefore': serialize.iso8601_datetime(date_created_before),
            'Track': track,
            'Publisher': publisher,
            'Kind': kind,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return SubscribedTrackPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of SubscribedTrackInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SubscribedTrackInstance
        :rtype: twilio.rest.video.v1.room.room_participant.room_participant_subscribed_track.SubscribedTrackPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return SubscribedTrackPage(self._version, response, self._solution)

    def update(self, track=values.unset, publisher=values.unset, kind=values.unset,
               status=values.unset):
        """
        Update the SubscribedTrackInstance

        :param unicode track: The track
        :param unicode publisher: The publisher
        :param SubscribedTrackInstance.Kind kind: The kind
        :param SubscribedTrackInstance.Status status: The status

        :returns: Updated SubscribedTrackInstance
        :rtype: twilio.rest.video.v1.room.room_participant.room_participant_subscribed_track.SubscribedTrackInstance
        """
        data = values.of({'Track': track, 'Publisher': publisher, 'Kind': kind, 'Status': status, })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return SubscribedTrackInstance(
            self._version,
            payload,
            room_sid=self._solution['room_sid'],
            subscriber_sid=self._solution['subscriber_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Video.V1.SubscribedTrackList>'


class SubscribedTrackPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the SubscribedTrackPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param room_sid: The room_sid
        :param subscriber_sid: The subscriber_sid

        :returns: twilio.rest.video.v1.room.room_participant.room_participant_subscribed_track.SubscribedTrackPage
        :rtype: twilio.rest.video.v1.room.room_participant.room_participant_subscribed_track.SubscribedTrackPage
        """
        super(SubscribedTrackPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of SubscribedTrackInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.video.v1.room.room_participant.room_participant_subscribed_track.SubscribedTrackInstance
        :rtype: twilio.rest.video.v1.room.room_participant.room_participant_subscribed_track.SubscribedTrackInstance
        """
        return SubscribedTrackInstance(
            self._version,
            payload,
            room_sid=self._solution['room_sid'],
            subscriber_sid=self._solution['subscriber_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Video.V1.SubscribedTrackPage>'


class SubscribedTrackInstance(InstanceResource):
    """  """

    class Kind(object):
        AUDIO = "audio"
        VIDEO = "video"
        DATA = "data"

    class Status(object):
        SUBSCRIBE = "subscribe"
        UNSUBSCRIBE = "unsubscribe"

    def __init__(self, version, payload, room_sid, subscriber_sid):
        """
        Initialize the SubscribedTrackInstance

        :returns: twilio.rest.video.v1.room.room_participant.room_participant_subscribed_track.SubscribedTrackInstance
        :rtype: twilio.rest.video.v1.room.room_participant.room_participant_subscribed_track.SubscribedTrackInstance
        """
        super(SubscribedTrackInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'room_sid': payload['room_sid'],
            'name': payload['name'],
            'publisher_sid': payload['publisher_sid'],
            'subscriber_sid': payload['subscriber_sid'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'enabled': payload['enabled'],
            'kind': payload['kind'],
        }

        # Context
        self._context = None
        self._solution = {'room_sid': room_sid, 'subscriber_sid': subscriber_sid, }

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def room_sid(self):
        """
        :returns: The room_sid
        :rtype: unicode
        """
        return self._properties['room_sid']

    @property
    def name(self):
        """
        :returns: The name
        :rtype: unicode
        """
        return self._properties['name']

    @property
    def publisher_sid(self):
        """
        :returns: The publisher_sid
        :rtype: unicode
        """
        return self._properties['publisher_sid']

    @property
    def subscriber_sid(self):
        """
        :returns: The subscriber_sid
        :rtype: unicode
        """
        return self._properties['subscriber_sid']

    @property
    def date_created(self):
        """
        :returns: The date_created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date_updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def enabled(self):
        """
        :returns: The enabled
        :rtype: bool
        """
        return self._properties['enabled']

    @property
    def kind(self):
        """
        :returns: The kind
        :rtype: SubscribedTrackInstance.Kind
        """
        return self._properties['kind']

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Video.V1.SubscribedTrackInstance>'