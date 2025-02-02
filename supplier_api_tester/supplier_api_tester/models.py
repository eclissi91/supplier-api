from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional, List, Dict


@dataclass
class TestResult:
    title: str = ''
    status: int = 0
    message: Optional[str] = None
    duration: int = 0

    @property
    def status_text(self):
        return {
            0: 'OK',
            1: 'WARNING',
            2: 'ERROR',
        }[self.status]

    @property
    def is_ok(self):
        return self.status == 0

    @property
    def is_warning(self):
        return self.status == 1

    @property
    def is_error(self):
        return self.status == 2


@dataclass
class DailyAvailability:
    date: date
    max_tickets: int


@dataclass
class Variant:
    id: str
    max_tickets: int
    name: str


@dataclass
class DailyVariants:
    date: date
    max_tickets: int
    variants: List[Variant]


@dataclass
class Timeslot:
    date: date
    start: str
    end: str
    max_tickets: int
    variants: List[Variant]


@dataclass
class ApiError:
    error: str
    error_code: int
    message: str


@dataclass
class Reservation:
    reservation_id: str
    expires_at: datetime


@dataclass
class Booking:
    booking_id: str
    barcode_format: str
    barcode_position: str
    barcode: Optional[str]
    tickets: Optional[Dict[str, List[str]]]
