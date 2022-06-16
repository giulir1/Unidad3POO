from zope.interface import Interface


class IDirector(Interface):

    def modificarBasico(self, cuil, nuevoBasico):
        pass

    def modificarPorcentajePorCargo(self, cuil, nuevoProcentaje):
        pass

    def modificarPorcentajePorCategoria(self, cuil, nuevoPorcentaje):
        pass

    def modificarImporteExtra(self, cuil, nuevoImporteExtra):
        pass
