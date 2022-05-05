from character.attribute import PugAttribute
from character.color import PugColor
from character.shape import PugShape
from pixart import abstract


class Pug(abstract.Character):
    """Register pug's blueprints."""

    ctype = "Pug"

    @property
    def shape(self):
        return self._shape

    @property
    def color(self):
        return self._color

    @property
    def attributes(self):
        return self._attr

    def create(self, num, **kwargs):
        self.num = num
        kwargs.setdefault("shape", {})
        kwargs.setdefault("color", {})
        kwargs.setdefault("skin", kwargs.get("skin"))
        kwargs.setdefault("attributes", {})

        self.makeShape(**kwargs["shape"])
        self.makeColor(skin=kwargs["skin"])
        self.makeAttributes(**kwargs["attributes"])

    def makeShape(self, **kwargs):
        self._shape = PugShape(**kwargs)

    def makeColor(self, **kwargs):
        self._color = PugColor(**kwargs)

    def makeAttributes(self, **kwargs):
        self._attr = PugAttribute(self, **kwargs)


class AnonyPug(Pug):
    """Register anonypug's blueprints."""

    ctype = "AnonyPug"

    def makeAttributes(self, **kwargs):
        kwargs["mask"] = "Anonymous"
        kwargs["mouth"] = False
        kwargs["eyes"] = False
        kwargs["glasses"] = False
        kwargs["nose"] = False
        kwargs["headband"] = False
        self._attr = PugAttribute(self, **kwargs)


class SleepingPug(Pug):
    """Register sleeping-pug's blueprints."""

    ctype = "SleepingPug"

    def makeShape(self, **kwargs):
        kwargs["eyes"] = "sleeping"
        kwargs["mouth"] = "sleeping"
        self._shape = PugShape(**kwargs)

    def makeAttributes(self, **kwargs):
        kwargs["mouth"] = False
        # kwargs["glasses"] = False
        self._attr = PugAttribute(self, **kwargs)


class KabukiPug(Pug):
    """Register kabuki-pug's blueprints."""

    ctype = "KabukiPug"

    def makeShape(self, **kwargs):
        kwargs["eyes"] = False
        self._shape = PugShape(**kwargs)

    def makeColor(self, **kwargs):
        kwargs["skin"] = "kabuki"
        self._color = PugColor(**kwargs)


class PhantomPug(Pug):
    """Register phantom-pug's blueprints."""

    ctype = "PhantomPug"

    def makeAttributes(self, **kwargs):
        kwargs["mask"] = "Phantom"
        self._attr = PugAttribute(self, **kwargs)
