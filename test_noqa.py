from typing import NamedTuple


class Bbox(NamedTuple):
    city_id: int
    lonmin: float
    latmin: float
    lonmax: float
    latmax: float

    @property  # noqa TYP004
    def enlarged(self) -> 'Bbox':
        '''return the class enlarged by 0.1 dec deg'''
        box_enlarged = Bbox(
            city_id=self.city_id,
            lonmin=self.lonmin + 0.1,
            latmin=self.latmin + 0.1,
            lonmax=self.lonmax + 0.1,
            latmax=self.latmax + 0.1,
        )
        return box_enlarged
