# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Tianqi(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.header = Tianqi.Header(self._io, self, self._root)
        self.unknown_blocks = Tianqi.UnknownBlocks(self._io, self, self._root)
        self.timestamp = Tianqi.Timestamp(self._io, self, self._root)
        self.orbital_data = Tianqi.OrbitalData(self._io, self, self._root)
        self.padding = self._io.read_bytes_full()

    class OrbitalElements(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.semi_major_axis = self._io.read_f4be()
            self.eccentricity = self._io.read_f4be()
            self.inclination = self._io.read_f4be()
            self.ascending_node = self._io.read_f4be()
            self.angle_x = self._io.read_f4be()
            self.angle_y = self._io.read_f4be()


    class UnknownBlocks(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.block1 = Tianqi.UnknownBlock1(self._io, self, self._root)
            self.block2 = Tianqi.UnknownBlock2(self._io, self, self._root)
            self.block3 = Tianqi.UnknownBlock3(self._io, self, self._root)


    class Timestamp(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.last_rx_time = self._io.read_u4be()
            self.unknown13 = self._io.read_u1()
            self.unknown14 = self._io.read_u1()


    class UnknownBlock1(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.unknown3 = self._io.read_u1()
            self.unknown4 = self._io.read_u1()
            self.unknown5 = self._io.read_u1()
            self.unknown6 = self._io.read_u1()
            self.unknown7 = self._io.read_u1()
            self.unknown8 = self._io.read_u1()
            self.unknown9 = self._io.read_u1()


    class OrbitalData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.set1 = Tianqi.OrbitalElements(self._io, self, self._root)
            self.set2 = Tianqi.OrbitalElements(self._io, self, self._root)


    class UnknownBlock2(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.unknown10_1 = self._io.read_u1()
            self.unknown10_2 = self._io.read_u1()
            self.unknown10_3 = self._io.read_u1()


    class Header(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.net_id = self._io.read_u1()
            self.message_type_id = self._io.read_u1()
            self.head_unknown = self._io.read_u1()
            self.sat_timestamp = self._io.read_u4be()
            self.sat_id = self._io.read_u1()


    class UnknownBlock3(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.unknown11_1 = self._io.read_u1()
            self.unknown11_2 = self._io.read_u1()
            self.unknown11_3 = self._io.read_u1()
            self.unknown11_4 = self._io.read_u1()
            self.unknown11_5 = self._io.read_u1()
            self.unknown11_6 = self._io.read_u1()
            self.unknown12_1 = self._io.read_u1()
            self.unknown12_2 = self._io.read_u1()
            self.unknown12_3 = self._io.read_u1()
            self.unknown12_4 = self._io.read_u1()



