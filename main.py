
from scripts.gamegui import GraphicsInterface
from scripts.matchapp import MatchApp

inter = GraphicsInterface()
app = MatchApp(inter)
app.run()
