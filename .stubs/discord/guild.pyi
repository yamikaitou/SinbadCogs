import datetime
from typing import Any, Dict, Iterator, List, NamedTuple, Optional, Tuple, Union

from typing_extensions import Literal

from .abc import Snowflake
from .asset import Asset
from .channel import CategoryChannel, StoreChannel, TextChannel, VoiceChannel
from .colour import Colour
from .emoji import Emoji
from .enums import (
    AuditLogAction,
    ContentFilter,
    NotificationLevel,
    VerificationLevel,
    VoiceRegion,
)
from .invite import Invite
from .iterators import AuditLogIterator, MemberIterator
from .member import Member
from .mixins import Hashable
from .permissions import PermissionOverwrite, Permissions
from .role import Role
from .user import User
from .voice_client import VoiceClient
from .webhook import Webhook
from .widget import Widget

_VALID_STATIC_ICON_FORMATS = Literal["jpeg", "jpg", "webp", "png"]
_VALID_ANIMATED_ICON_FORMATS = Literal[_VALID_STATIC_ICON_FORMATS, "gif"]

class BanEntry(NamedTuple):
    user: User
    reason: str

class SystemChannelFlags:
    value: int
    join_notifications: bool
    premium_subscriptions: bool
    def __init__(
        self, *, join_notifications: bool = ..., premium_subscriptions: bool = ...
    ) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    def __iter__(self) -> Iterator[Tuple[str, bool]]: ...

class Guild(Hashable):
    name: str
    emojis: Tuple[Emoji, ...]
    region: VoiceRegion
    afk_timeout: int
    afk_channel: Optional[VoiceChannel]
    icon: Optional[str]
    id: int
    owner_id: int
    unavailable: bool
    max_presences: Optional[int]
    max_members: Optional[int]
    banner: Optional[str]
    description: Optional[str]
    mfa_level: int
    verification_level: VerificationLevel
    default_notifications: NotificationLevel
    explicit_content_filter: ContentFilter
    features: List[str]
    splash: Optional[str]
    premium_tier: int
    premium_subscription_count: int
    preferred_locale: Optional[str]
    @property
    def channels(
        self,
    ) -> List[Union[TextChannel, VoiceChannel, CategoryChannel, StoreChannel]]: ...
    @property
    def large(self) -> bool: ...
    @property
    def voice_channels(self) -> List[VoiceChannel]: ...
    @property
    def me(self) -> Member: ...
    @property
    def voice_client(self) -> VoiceClient: ...
    @property
    def text_channels(self) -> List[TextChannel]: ...
    @property
    def categories(self) -> List[CategoryChannel]: ...
    def by_category(
        self,
    ) -> List[
        Tuple[
            Optional[CategoryChannel],
            List[Union[TextChannel, VoiceChannel, StoreChannel]],
        ]
    ]: ...
    def get_channel(
        self, channel_id: int
    ) -> Optional[Union[TextChannel, VoiceChannel, StoreChannel, CategoryChannel]]: ...
    @property
    def system_channel(self) -> Optional[TextChannel]: ...
    @property
    def system_channel_flags(self) -> SystemChannelFlags: ...
    @property
    def emoji_limit(self) -> int: ...
    @property
    def bitrate_limit(self) -> float: ...
    @property
    def filesize_limit(self) -> int: ...
    @property
    def members(self) -> List[Member]: ...
    def get_member(self, user_id: int) -> Optional[Member]: ...
    @property
    def premium_subscribers(self) -> List[Member]: ...
    @property
    def roles(self) -> List[Role]: ...
    def get_role(self, role_id: int) -> Optional[Role]: ...
    @property
    def default_role(self) -> Role: ...
    @property
    def owner(self) -> Member: ...
    @property
    def icon_url(self) -> Asset: ...
    def is_icon_animated(self) -> bool: ...
    def icon_url_as(
        self,
        *,
        format: Optional[_VALID_ANIMATED_ICON_FORMATS] = ...,
        static_format: _VALID_STATIC_ICON_FORMATS = ...,
        size: int = ...,
    ) -> Asset: ...
    @property
    def banner_url(self) -> Asset: ...
    def banner_url_as(
        self, *, format: _VALID_STATIC_ICON_FORMATS = ..., size: int = ...
    ) -> Asset: ...
    @property
    def splash_url(self) -> Asset: ...
    def splash_url_as(
        self, *, format: _VALID_STATIC_ICON_FORMATS = ..., size: int = ...
    ) -> Asset: ...
    @property
    def member_count(self) -> int: ...
    @property
    def chunked(self) -> bool: ...
    @property
    def shard_id(self) -> Optional[int]: ...
    @property
    def created_at(self) -> datetime.datetime: ...
    def get_member_named(self, name: str) -> Optional[Member]: ...
    async def create_text_channel(
        self,
        name: str,
        *,
        overwrites: Optional[Dict[Union[Role, Member], PermissionOverwrite]] = ...,
        category: Optional[CategoryChannel] = ...,
        position: int = ...,
        topic: str = ...,
        slowmode_delay: int = ...,
        nsfw: bool = ...,
        reason: Optional[str] = ...,
    ) -> TextChannel: ...
    async def create_voice_channel(
        self,
        name: str,
        *,
        overwrites: Optional[Dict[Union[Role, Member], PermissionOverwrite]] = ...,
        category: Optional[CategoryChannel] = ...,
        bitrate: int = ...,
        position: int = ...,
        user_limit: int = ...,
        reason: Optional[str] = ...,
    ) -> VoiceChannel: ...
    async def create_category(
        self,
        name: str,
        *,
        overwrites: Optional[Dict[Union[Role, Member], PermissionOverwrite]] = ...,
        position: int = ...,
        reason: Optional[str] = ...,
    ) -> CategoryChannel: ...
    async def leave(self) -> None: ...
    async def delete(self) -> None: ...
    async def edit(
        self,
        *,
        reason: Optional[str] = ...,
        name: str = ...,
        description: str = ...,
        icon: Optional[bytes] = ...,
        splash: Optional[bytes] = ...,
        banner: Optional[bytes] = ...,
        region: VoiceRegion = ...,
        afk_channel: Optional[VoiceChannel] = ...,
        afk_timeout: int = ...,
        owner: Member = ...,
        verification_level: VerificationLevel = ...,
        default_notifications: NotificationLevel = ...,
        explicit_content_filter: ContentFilter = ...,
        vanity_code: str = ...,
        system_channel: Optional[TextChannel] = ...,
        system_channel_flags: SystemChannelFlags = ...,
    ) -> None: ...
    async def fetch_channels(
        self,
    ) -> List[Union[TextChannel, VoiceChannel, StoreChannel, CategoryChannel]]: ...
    async def fetch_members(
        self,
        *,
        limit: int = ...,
        after: Optional[Union[Snowflake, datetime.datetime]] = ...,
    ) -> MemberIterator: ...
    async def fetch_member(self, member_id: int) -> Member: ...
    async def fetch_ban(self, user: Snowflake) -> BanEntry: ...
    async def bans(self) -> List[BanEntry]: ...
    async def prune_members(
        self, *, days: int, compute_prune_count: bool = ..., reason: Optional[str] = ...
    ) -> Optional[int]: ...
    async def webhooks(self) -> List[Webhook]: ...
    async def estimate_pruned_members(self, *, days: int) -> int: ...
    async def invites(self) -> List[Invite]: ...
    async def fetch_emojis(self) -> List[Emoji]: ...
    async def fetch_emoji(self, emoji_id: int) -> Emoji: ...
    async def create_custom_emoji(
        self, *, name: str, image: Union[bytes, bytearray], reason: Optional[str] = ...
    ) -> Emoji: ...
    async def fetch_roles(self) -> List[Role]: ...
    async def create_role(
        self,
        *,
        name: str,
        permissions: Permissions = ...,
        colour: Colour = ...,
        color: Colour = ...,
        hoist: bool = ...,
        mentionable: bool = ...,
        reason: Optional[str] = ...,
    ) -> Role: ...
    async def kick(self, user: Snowflake, *, reason: Optional[str] = ...) -> None: ...
    async def ban(
        self,
        user: Snowflake,
        *,
        reason: Optional[str] = ...,
        delete_message_days: int = ...,
    ) -> None: ...
    async def unban(self, user: Snowflake, *, reason: Optional[str] = ...) -> None: ...
    async def vanity_invite(self) -> Invite: ...
    def ack(self) -> Any: ...
    def audit_logs(
        self,
        *,
        limit: int = ...,
        before: Optional[Union[Snowflake, datetime.datetime]] = ...,
        after: Optional[Union[Snowflake, datetime.datetime]] = ...,
        oldest_first: Optional[bool] = ...,
        user: Optional[Snowflake] = ...,
        action: Optional[AuditLogAction] = ...,
    ) -> AuditLogIterator: ...
    async def widget(self) -> Widget: ...
    async def query_members(
        self, query: str, *, limit: int = ..., cache: bool = ...
    ) -> List[Member]: ...
