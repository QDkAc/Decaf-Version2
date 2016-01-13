VTABLE(_Main) {
    <empty>
    Main
}

VTABLE(_Sorted) {
    <empty>
    Sorted
    _Sorted.init;
    _Sorted.print;
    _Sorted.merge;
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T8 = 4
    parm _T8
    _T9 =  call _Alloc
    _T10 = VTBL <_Main>
    *(_T9 + 0) = _T10
    return _T9
}

FUNCTION(_Sorted_New) {
memo ''
_Sorted_New:
    _T11 = 12
    parm _T11
    _T12 =  call _Alloc
    _T13 = 0
    *(_T12 + 4) = _T13
    *(_T12 + 8) = _T13
    _T14 = VTBL <_Sorted>
    *(_T12 + 0) = _T14
    return _T12
}

FUNCTION(_Main.sort) {
memo '_T0:4 _T1:8 _T2:12'
_Main.sort:
    _T15 = 1
    _T16 = (_T1 + _T15)
    _T17 = (_T16 >= _T2)
    if (_T17 == 0) branch _L15
    _T19 =  call _Sorted_New
    _T18 = _T19
    _T20 = *(_T0 + 0)
    _T21 = (_T1 < _T20)
    if (_T21 == 0) branch _L16
    _T22 = 0
    _T23 = (_T1 < _T22)
    if (_T23 == 0) branch _L17
_L16:
    _T24 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T24
    call _PrintString
    call _Halt
_L17:
    _T25 = 4
    _T26 = (_T1 * _T25)
    _T27 = (_T26 + _T25)
    _T28 = *(_T0 + _T27)
    parm _T18
    parm _T28
    _T29 = *(_T18 + 0)
    _T30 = *(_T29 + 8)
    call _T30
    return _T18
_L15:
    _T32 = (_T1 + _T2)
    _T33 = 1
    _T34 = (_T32 + _T33)
    _T35 = 2
    _T36 = 0
    _T37 = (_T35 == _T36)
    if (_T37 == 0) branch _L18
    _T38 = "Decaf runtime error: Division by zero error."
    parm _T38
    call _PrintString
    call _Halt
_L18:
    _T39 = (_T34 / _T35)
    _T31 = _T39
    parm _T0
    parm _T1
    parm _T31
    _T41 =  call _Main.sort
    _T40 = _T41
    parm _T0
    parm _T31
    parm _T2
    _T42 =  call _Main.sort
    parm _T40
    parm _T42
    _T43 = *(_T40 + 0)
    _T44 = *(_T43 + 16)
    call _T44
    return _T40
}

FUNCTION(main) {
memo ''
main:
    _T47 = 1024
    _T46 = _T47
    _T48 = 0
    _T49 = (_T46 < _T48)
    if (_T49 == 0) branch _L19
    _T50 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T50
    call _PrintString
    call _Halt
_L19:
    _T51 = 4
    _T52 = (_T51 * _T46)
    _T53 = (_T51 + _T52)
    parm _T53
    _T54 =  call _Alloc
    *(_T54 + 0) = _T46
    _T45 = _T54
    _T56 = 0
    _T55 = _T56
_L20:
    _T57 = (_T55 < _T46)
    if (_T57 == 0) branch _L21
    _T58 = *(_T45 + 0)
    _T59 = (_T55 < _T58)
    if (_T59 == 0) branch _L22
    _T60 = 0
    _T61 = (_T55 < _T60)
    if (_T61 == 0) branch _L23
_L22:
    _T62 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T62
    call _PrintString
    call _Halt
_L23:
    _T63 = 4
    _T64 = (_T55 * _T63)
    _T65 = (_T64 + _T63)
    _T66 = *(_T45 + _T65)
    _T67 = 4
    _T68 = (_T55 * _T67)
    _T69 = (_T68 + _T67)
    *(_T45 + _T69) = _T55
    _T70 = 1
    _T71 = (_T55 + _T70)
    _T55 = _T71
    branch _L20
_L21:
    _T73 = 0
    parm _T45
    parm _T73
    parm _T46
    _T74 =  call _Main.sort
    _T72 = _T74
    parm _T72
    _T75 = *(_T72 + 0)
    _T76 = *(_T75 + 12)
    call _T76
}

FUNCTION(_Sorted.init) {
memo '_T3:4 _T4:8'
_Sorted.init:
    _T77 = 1
    _T78 = 0
    _T79 = (_T77 < _T78)
    if (_T79 == 0) branch _L24
    _T80 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T80
    call _PrintString
    call _Halt
_L24:
    _T81 = 4
    _T82 = (_T81 * _T77)
    _T83 = (_T81 + _T82)
    parm _T83
    _T84 =  call _Alloc
    *(_T84 + 0) = _T77
    _T85 = *(_T3 + 4)
    *(_T3 + 4) = _T84
    _T86 = *(_T3 + 4)
    _T87 = 0
    _T88 = *(_T86 + 0)
    _T89 = (_T87 < _T88)
    if (_T89 == 0) branch _L25
    _T90 = 0
    _T91 = (_T87 < _T90)
    if (_T91 == 0) branch _L26
_L25:
    _T92 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T92
    call _PrintString
    call _Halt
_L26:
    _T93 = 4
    _T94 = (_T87 * _T93)
    _T95 = (_T94 + _T93)
    _T96 = *(_T86 + _T95)
    _T97 = 4
    _T98 = (_T87 * _T97)
    _T99 = (_T98 + _T97)
    *(_T86 + _T99) = _T4
    _T100 = 1
    _T101 = *(_T3 + 8)
    *(_T3 + 8) = _T100
}

FUNCTION(_Sorted.print) {
memo '_T5:4'
_Sorted.print:
    _T102 = *(_T5 + 4)
    _T103 = 0
    _T104 = *(_T102 + 0)
    _T105 = (_T103 < _T104)
    if (_T105 == 0) branch _L27
    _T106 = 0
    _T107 = (_T103 < _T106)
    if (_T107 == 0) branch _L28
_L27:
    _T108 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T108
    call _PrintString
    call _Halt
_L28:
    _T109 = 4
    _T110 = (_T103 * _T109)
    _T111 = (_T110 + _T109)
    _T112 = *(_T102 + _T111)
    parm _T112
    call _PrintInt
    _T113 = " "
    parm _T113
    call _PrintString
    _T114 = *(_T5 + 8)
    parm _T114
    call _PrintInt
    _T115 = "\n"
    parm _T115
    call _PrintString
}

FUNCTION(_Sorted.merge) {
memo '_T6:4 _T7:8'
_Sorted.merge:
    _T117 = *(_T6 + 8)
    _T118 = *(_T7 + 8)
    _T119 = (_T117 + _T118)
    _T120 = 0
    _T121 = (_T119 < _T120)
    if (_T121 == 0) branch _L29
    _T122 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T122
    call _PrintString
    call _Halt
_L29:
    _T123 = 4
    _T124 = (_T123 * _T119)
    _T125 = (_T123 + _T124)
    parm _T125
    _T126 =  call _Alloc
    *(_T126 + 0) = _T119
    _T116 = _T126
    _T130 = 0
    _T127 = _T130
    _T131 = 0
    _T128 = _T131
_L30:
    _T132 = (_T127 + _T128)
    _T133 = *(_T6 + 8)
    _T134 = *(_T7 + 8)
    _T135 = (_T133 + _T134)
    _T136 = (_T132 < _T135)
    if (_T136 == 0) branch _L31
    _T137 = *(_T6 + 8)
    _T138 = (_T127 == _T137)
    if (_T138 == 0) branch _L32
    _T139 = *(_T7 + 4)
    _T140 = *(_T139 + 0)
    _T141 = (_T128 < _T140)
    if (_T141 == 0) branch _L33
    _T142 = 0
    _T143 = (_T128 < _T142)
    if (_T143 == 0) branch _L34
_L33:
    _T144 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T144
    call _PrintString
    call _Halt
_L34:
    _T145 = 4
    _T146 = (_T128 * _T145)
    _T147 = (_T146 + _T145)
    _T148 = *(_T139 + _T147)
    _T149 = (_T127 + _T128)
    _T150 = *(_T116 + 0)
    _T151 = (_T149 < _T150)
    if (_T151 == 0) branch _L35
    _T152 = 0
    _T153 = (_T149 < _T152)
    if (_T153 == 0) branch _L36
_L35:
    _T154 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T154
    call _PrintString
    call _Halt
_L36:
    _T155 = 4
    _T156 = (_T149 * _T155)
    _T157 = (_T156 + _T155)
    _T158 = *(_T116 + _T157)
    _T159 = 4
    _T160 = (_T149 * _T159)
    _T161 = (_T160 + _T159)
    *(_T116 + _T161) = _T148
    _T162 = 1
    _T163 = (_T128 + _T162)
    _T128 = _T163
    branch _L37
_L32:
    _T164 = *(_T7 + 8)
    _T165 = (_T128 == _T164)
    if (_T165 == 0) branch _L38
    _T166 = *(_T6 + 4)
    _T167 = *(_T166 + 0)
    _T168 = (_T127 < _T167)
    if (_T168 == 0) branch _L39
    _T169 = 0
    _T170 = (_T127 < _T169)
    if (_T170 == 0) branch _L40
_L39:
    _T171 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T171
    call _PrintString
    call _Halt
_L40:
    _T172 = 4
    _T173 = (_T127 * _T172)
    _T174 = (_T173 + _T172)
    _T175 = *(_T166 + _T174)
    _T176 = (_T127 + _T128)
    _T177 = *(_T116 + 0)
    _T178 = (_T176 < _T177)
    if (_T178 == 0) branch _L41
    _T179 = 0
    _T180 = (_T176 < _T179)
    if (_T180 == 0) branch _L42
_L41:
    _T181 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T181
    call _PrintString
    call _Halt
_L42:
    _T182 = 4
    _T183 = (_T176 * _T182)
    _T184 = (_T183 + _T182)
    _T185 = *(_T116 + _T184)
    _T186 = 4
    _T187 = (_T176 * _T186)
    _T188 = (_T187 + _T186)
    *(_T116 + _T188) = _T175
    _T189 = 1
    _T190 = (_T127 + _T189)
    _T127 = _T190
    branch _L43
_L38:
    _T191 = *(_T6 + 4)
    _T192 = *(_T191 + 0)
    _T193 = (_T127 < _T192)
    if (_T193 == 0) branch _L44
    _T194 = 0
    _T195 = (_T127 < _T194)
    if (_T195 == 0) branch _L45
_L44:
    _T196 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T196
    call _PrintString
    call _Halt
_L45:
    _T197 = 4
    _T198 = (_T127 * _T197)
    _T199 = (_T198 + _T197)
    _T200 = *(_T191 + _T199)
    _T201 = *(_T7 + 4)
    _T202 = *(_T201 + 0)
    _T203 = (_T128 < _T202)
    if (_T203 == 0) branch _L46
    _T204 = 0
    _T205 = (_T128 < _T204)
    if (_T205 == 0) branch _L47
_L46:
    _T206 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T206
    call _PrintString
    call _Halt
_L47:
    _T207 = 4
    _T208 = (_T128 * _T207)
    _T209 = (_T208 + _T207)
    _T210 = *(_T201 + _T209)
    _T211 = (_T200 < _T210)
    if (_T211 == 0) branch _L48
    _T212 = *(_T7 + 4)
    _T213 = *(_T212 + 0)
    _T214 = (_T128 < _T213)
    if (_T214 == 0) branch _L49
    _T215 = 0
    _T216 = (_T128 < _T215)
    if (_T216 == 0) branch _L50
_L49:
    _T217 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T217
    call _PrintString
    call _Halt
_L50:
    _T218 = 4
    _T219 = (_T128 * _T218)
    _T220 = (_T219 + _T218)
    _T221 = *(_T212 + _T220)
    _T222 = (_T127 + _T128)
    _T223 = *(_T116 + 0)
    _T224 = (_T222 < _T223)
    if (_T224 == 0) branch _L51
    _T225 = 0
    _T226 = (_T222 < _T225)
    if (_T226 == 0) branch _L52
_L51:
    _T227 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T227
    call _PrintString
    call _Halt
_L52:
    _T228 = 4
    _T229 = (_T222 * _T228)
    _T230 = (_T229 + _T228)
    _T231 = *(_T116 + _T230)
    _T232 = 4
    _T233 = (_T222 * _T232)
    _T234 = (_T233 + _T232)
    *(_T116 + _T234) = _T221
    _T235 = 1
    _T236 = (_T128 + _T235)
    _T128 = _T236
_L48:
_L43:
_L37:
    branch _L30
_L31:
    _T237 = *(_T6 + 4)
    *(_T6 + 4) = _T116
    _T238 = *(_T6 + 8)
    _T239 = *(_T7 + 8)
    _T240 = (_T238 + _T239)
    _T241 = *(_T6 + 8)
    *(_T6 + 8) = _T240
}
