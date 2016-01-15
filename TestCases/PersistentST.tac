VTABLE(_Main) {
    <empty>
    Main
}

VTABLE(_Node) {
    <empty>
    Node
    _Node.set;
    _Node.update;
    _Node.init;
    _Node.query;
    _Node.change;
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T17 = 4
    parm _T17
    _T18 =  call _Alloc
    _T19 = VTBL <_Main>
    *(_T18 + 0) = _T19
    return _T18
}

FUNCTION(_Node_New) {
memo ''
_Node_New:
    _T20 = 24
    parm _T20
    _T21 =  call _Alloc
    _T22 = VTBL <_Node>
    *(_T21 + 0) = _T22
    return _T21
}

FUNCTION(_Main.rand) {
memo '_T0:4'
_Main.rand:
    _T23 = 17
    _T24 = (_T23 * _T0)
    _T25 = (_T24 * _T0)
    _T26 = 131
    _T27 = (_T26 * _T0)
    _T28 = (_T25 + _T27)
    _T29 = 45
    _T30 = (_T28 + _T29)
    return _T30
}

FUNCTION(_Main.get) {
memo '_T1:4 _T2:8'
_Main.get:
    _T31 = 0
    _T32 = (_T2 == _T31)
    if (_T32 == 0) branch _L18
    _T33 = "Decaf runtime error: Division by zero error."
    parm _T33
    call _PrintString
    call _Halt
_L18:
    _T34 = (_T1 % _T2)
    _T1 = _T34
    _T35 = 0
    _T36 = (_T1 < _T35)
    if (_T36 == 0) branch _L19
    _T37 = (_T1 + _T2)
    _T1 = _T37
_L19:
    return _T1
}

FUNCTION(main) {
memo ''
main:
    _T41 = 100000
    _T40 = _T41
    _T42 = 1000
    _T38 = _T42
    _T43 = 0
    _T44 = (_T38 < _T43)
    if (_T44 == 0) branch _L20
    _T45 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T45
    call _PrintString
    call _Halt
_L20:
    _T46 = 4
    _T47 = (_T46 * _T38)
    _T48 = (_T46 + _T47)
    parm _T48
    _T49 =  call _Alloc
    *(_T49 + 0) = _T38
    _T39 = _T49
    _T52 = 199581
    _T51 = _T52
    _T53 = 0
    _T50 = _T53
    branch _L21
_L22:
    _T54 = 1
    _T55 = (_T50 + _T54)
    _T50 = _T55
_L21:
    _T56 = (_T50 < _T38)
    if (_T56 == 0) branch _L23
    parm _T51
    parm _T40
    _T57 =  call _Main.get
    _T58 = *(_T39 + 0)
    _T59 = (_T50 < _T58)
    if (_T59 == 0) branch _L24
    _T60 = 0
    _T61 = (_T50 < _T60)
    if (_T61 == 0) branch _L25
_L24:
    _T62 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T62
    call _PrintString
    call _Halt
_L25:
    _T63 = 4
    _T64 = (_T50 * _T63)
    _T65 = (_T64 + _T63)
    _T66 = *(_T39 + _T65)
    _T67 = 4
    _T68 = (_T50 * _T67)
    _T69 = (_T68 + _T67)
    *(_T39 + _T69) = _T57
    parm _T51
    _T70 =  call _Main.rand
    _T51 = _T70
    branch _L22
_L23:
    _T72 =  call _Node_New
    _T71 = _T72
    _T73 = 0
    parm _T71
    parm _T73
    parm _T38
    parm _T39
    _T74 = *(_T71 + 0)
    _T75 = *(_T74 + 16)
    call _T75
    _T76 = 0
    _T50 = _T76
    branch _L26
_L27:
    _T77 = 1
    _T78 = (_T50 + _T77)
    _T50 = _T78
_L26:
    _T79 = 10
    _T80 = (_T79 * _T38)
    _T81 = (_T50 < _T80)
    if (_T81 == 0) branch _L28
    parm _T51
    parm _T38
    _T84 =  call _Main.get
    _T82 = _T84
    parm _T51
    _T85 =  call _Main.rand
    _T51 = _T85
    parm _T51
    parm _T38
    _T86 =  call _Main.get
    _T83 = _T86
    parm _T51
    _T87 =  call _Main.rand
    _T51 = _T87
    _T88 = (_T82 > _T83)
    if (_T88 == 0) branch _L29
    _T89 = _T82
    _T82 = _T83
    _T83 = _T89
_L29:
    _T90 = 1
    _T91 = (_T83 + _T90)
    parm _T71
    parm _T82
    parm _T91
    _T92 = *(_T71 + 0)
    _T93 = *(_T92 + 20)
    _T94 =  call _T93
    parm _T94
    call _PrintInt
    _T95 = "\n"
    parm _T95
    call _PrintString
    parm _T51
    parm _T38
    _T97 =  call _Main.get
    _T96 = _T97
    parm _T51
    _T98 =  call _Main.rand
    _T51 = _T98
    parm _T51
    parm _T40
    _T100 =  call _Main.get
    _T99 = _T100
    parm _T71
    parm _T96
    parm _T99
    _T101 = *(_T71 + 0)
    _T102 = *(_T101 + 24)
    _T103 =  call _T102
    _T71 = _T103
    branch _L27
_L28:
}

FUNCTION(_Node.set) {
memo '_T3:4 _T4:8 _T5:12'
_Node.set:
    _T104 = *(_T3 + 12)
    *(_T3 + 12) = _T4
    _T105 = *(_T3 + 16)
    *(_T3 + 16) = _T5
}

FUNCTION(_Node.update) {
memo '_T6:4'
_Node.update:
    _T107 = *(_T6 + 4)
    _T108 = *(_T107 + 20)
    _T109 = *(_T6 + 8)
    _T110 = *(_T109 + 20)
    _T111 = (_T108 > _T110)
    if (_T111 == 0) branch _L30
    _T112 = *(_T6 + 4)
    _T113 = *(_T112 + 20)
    _T106 = _T113
    branch _L31
_L30:
    _T114 = *(_T6 + 8)
    _T115 = *(_T114 + 20)
    _T106 = _T115
_L31:
    _T116 = *(_T6 + 20)
    *(_T6 + 20) = _T106
}

FUNCTION(_Node.init) {
memo '_T7:4 _T8:8 _T9:12 _T10:16'
_Node.init:
    parm _T7
    parm _T8
    parm _T9
    _T117 = *(_T7 + 0)
    _T118 = *(_T117 + 8)
    call _T118
    _T119 = 1
    _T120 = (_T8 + _T119)
    _T121 = (_T120 == _T9)
    if (_T121 == 0) branch _L32
    _T122 = *(_T10 + 0)
    _T123 = (_T8 < _T122)
    if (_T123 == 0) branch _L33
    _T124 = 0
    _T125 = (_T8 < _T124)
    if (_T125 == 0) branch _L34
_L33:
    _T126 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T126
    call _PrintString
    call _Halt
_L34:
    _T127 = 4
    _T128 = (_T8 * _T127)
    _T129 = (_T128 + _T127)
    _T130 = *(_T10 + _T129)
    _T131 = *(_T7 + 20)
    *(_T7 + 20) = _T130
    return <empty>
_L32:
    _T132 =  call _Node_New
    _T133 = *(_T7 + 4)
    *(_T7 + 4) = _T132
    _T134 =  call _Node_New
    _T135 = *(_T7 + 8)
    *(_T7 + 8) = _T134
    _T137 = (_T8 + _T9)
    _T138 = 2
    _T139 = 0
    _T140 = (_T138 == _T139)
    if (_T140 == 0) branch _L35
    _T141 = "Decaf runtime error: Division by zero error."
    parm _T141
    call _PrintString
    call _Halt
_L35:
    _T142 = (_T137 / _T138)
    _T136 = _T142
    _T143 = *(_T7 + 4)
    parm _T143
    parm _T8
    parm _T136
    parm _T10
    _T144 = *(_T143 + 0)
    _T145 = *(_T144 + 16)
    call _T145
    _T146 = *(_T7 + 8)
    parm _T146
    parm _T136
    parm _T9
    parm _T10
    _T147 = *(_T146 + 0)
    _T148 = *(_T147 + 16)
    call _T148
    parm _T7
    _T149 = *(_T7 + 0)
    _T150 = *(_T149 + 12)
    call _T150
}

FUNCTION(_Node.query) {
memo '_T11:4 _T12:8 _T13:12'
_Node.query:
    _T151 = *(_T11 + 12)
    _T152 = (_T12 <= _T151)
    _T153 = *(_T11 + 16)
    _T154 = (_T13 >= _T153)
    _T155 = (_T152 && _T154)
    if (_T155 == 0) branch _L36
    _T156 = *(_T11 + 20)
    return _T156
_L36:
    _T157 = *(_T11 + 12)
    _T158 = (_T157 >= _T13)
    _T159 = *(_T11 + 16)
    _T160 = (_T12 >= _T159)
    _T161 = (_T158 || _T160)
    if (_T161 == 0) branch _L37
    _T162 = 1
    _T163 = - _T162
    return _T163
_L37:
    _T165 = *(_T11 + 4)
    parm _T165
    parm _T12
    parm _T13
    _T166 = *(_T165 + 0)
    _T167 = *(_T166 + 20)
    _T168 =  call _T167
    _T164 = _T168
    _T170 = *(_T11 + 8)
    parm _T170
    parm _T12
    parm _T13
    _T171 = *(_T170 + 0)
    _T172 = *(_T171 + 20)
    _T173 =  call _T172
    _T169 = _T173
    _T175 = (_T164 > _T169)
    if (_T175 == 0) branch _L38
    _T174 = _T164
    branch _L39
_L38:
    _T174 = _T169
_L39:
    return _T174
}

FUNCTION(_Node.change) {
memo '_T14:4 _T15:8 _T16:12'
_Node.change:
    _T176 = *(_T14 + 12)
    _T177 = (_T15 < _T176)
    _T178 = *(_T14 + 16)
    _T179 = (_T15 >= _T178)
    _T180 = (_T177 || _T179)
    if (_T180 == 0) branch _L40
    return _T14
_L40:
    _T182 =  call _Node_New
    _T181 = _T182
    _T183 = *(_T14 + 12)
    _T184 = *(_T14 + 16)
    parm _T181
    parm _T183
    parm _T184
    _T185 = *(_T181 + 0)
    _T186 = *(_T185 + 8)
    call _T186
    _T187 = *(_T14 + 12)
    _T188 = 1
    _T189 = (_T187 + _T188)
    _T190 = *(_T14 + 16)
    _T191 = (_T189 == _T190)
    if (_T191 == 0) branch _L41
    _T192 = *(_T181 + 20)
    *(_T181 + 20) = _T16
    return _T181
_L41:
    _T193 = *(_T14 + 4)
    parm _T193
    parm _T15
    parm _T16
    _T194 = *(_T193 + 0)
    _T195 = *(_T194 + 24)
    _T196 =  call _T195
    _T197 = *(_T181 + 4)
    *(_T181 + 4) = _T196
    _T198 = *(_T14 + 8)
    parm _T198
    parm _T15
    parm _T16
    _T199 = *(_T198 + 0)
    _T200 = *(_T199 + 24)
    _T201 =  call _T200
    _T202 = *(_T181 + 8)
    *(_T181 + 8) = _T201
    parm _T181
    _T203 = *(_T181 + 0)
    _T204 = *(_T203 + 12)
    call _T204
    return _T181
}

