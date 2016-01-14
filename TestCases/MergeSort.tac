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
    _T13 = VTBL <_Sorted>
    *(_T12 + 0) = _T13
    return _T12
}

FUNCTION(_Main.sort) {
memo '_T0:4 _T1:8 _T2:12'
_Main.sort:
    _T14 = 1
    _T15 = (_T1 + _T14)
    _T16 = (_T15 >= _T2)
    if (_T16 == 0) branch _L15
    _T18 =  call _Sorted_New
    _T17 = _T18
    _T19 = *(_T0 + 0)
    _T20 = (_T1 < _T19)
    if (_T20 == 0) branch _L16
    _T21 = 0
    _T22 = (_T1 < _T21)
    if (_T22 == 0) branch _L17
_L16:
    _T23 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T23
    call _PrintString
    call _Halt
_L17:
    _T24 = 4
    _T25 = (_T1 * _T24)
    _T26 = (_T25 + _T24)
    _T27 = *(_T0 + _T26)
    parm _T17
    parm _T27
    _T28 = *(_T17 + 0)
    _T29 = *(_T28 + 8)
    call _T29
    return _T17
_L15:
    _T31 = (_T1 + _T2)
    _T32 = 1
    _T33 = (_T31 + _T32)
    _T34 = 2
    _T35 = 0
    _T36 = (_T34 == _T35)
    if (_T36 == 0) branch _L18
    _T37 = "Decaf runtime error: Division by zero error."
    parm _T37
    call _PrintString
    call _Halt
_L18:
    _T38 = (_T33 / _T34)
    _T30 = _T38
    parm _T0
    parm _T1
    parm _T30
    _T40 =  call _Main.sort
    _T39 = _T40
    parm _T0
    parm _T30
    parm _T2
    _T41 =  call _Main.sort
    parm _T39
    parm _T41
    _T42 = *(_T39 + 0)
    _T43 = *(_T42 + 16)
    call _T43
    return _T39
}

FUNCTION(main) {
memo ''
main:
    _T46 = 100
    _T45 = _T46
    _T47 = 0
    _T48 = (_T45 < _T47)
    if (_T48 == 0) branch _L19
    _T49 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T49
    call _PrintString
    call _Halt
_L19:
    _T50 = 4
    _T51 = (_T50 * _T45)
    _T52 = (_T50 + _T51)
    parm _T52
    _T53 =  call _Alloc
    *(_T53 + 0) = _T45
    _T44 = _T53
    _T55 = 0
    _T54 = _T55
_L20:
    _T56 = (_T54 < _T45)
    if (_T56 == 0) branch _L21
    _T57 = *(_T44 + 0)
    _T58 = (_T54 < _T57)
    if (_T58 == 0) branch _L22
    _T59 = 0
    _T60 = (_T54 < _T59)
    if (_T60 == 0) branch _L23
_L22:
    _T61 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T61
    call _PrintString
    call _Halt
_L23:
    _T62 = 4
    _T63 = (_T54 * _T62)
    _T64 = (_T63 + _T62)
    _T65 = *(_T44 + _T64)
    _T66 = 4
    _T67 = (_T54 * _T66)
    _T68 = (_T67 + _T66)
    *(_T44 + _T68) = _T54
    _T69 = 1
    _T70 = (_T54 + _T69)
    _T54 = _T70
    branch _L20
_L21:
    _T72 = 0
    parm _T44
    parm _T72
    parm _T45
    _T73 =  call _Main.sort
    _T71 = _T73
    parm _T71
    _T74 = *(_T71 + 0)
    _T75 = *(_T74 + 12)
    call _T75
}

FUNCTION(_Sorted.init) {
memo '_T3:4 _T4:8'
_Sorted.init:
    _T76 = 1
    _T77 = 0
    _T78 = (_T76 < _T77)
    if (_T78 == 0) branch _L24
    _T79 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T79
    call _PrintString
    call _Halt
_L24:
    _T80 = 4
    _T81 = (_T80 * _T76)
    _T82 = (_T80 + _T81)
    parm _T82
    _T83 =  call _Alloc
    *(_T83 + 0) = _T76
    _T84 = *(_T3 + 4)
    *(_T3 + 4) = _T83
    _T85 = *(_T3 + 4)
    _T86 = 0
    _T87 = *(_T85 + 0)
    _T88 = (_T86 < _T87)
    if (_T88 == 0) branch _L25
    _T89 = 0
    _T90 = (_T86 < _T89)
    if (_T90 == 0) branch _L26
_L25:
    _T91 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T91
    call _PrintString
    call _Halt
_L26:
    _T92 = 4
    _T93 = (_T86 * _T92)
    _T94 = (_T93 + _T92)
    _T95 = *(_T85 + _T94)
    _T96 = 4
    _T97 = (_T86 * _T96)
    _T98 = (_T97 + _T96)
    *(_T85 + _T98) = _T4
    _T99 = 1
    _T100 = *(_T3 + 8)
    *(_T3 + 8) = _T99
}

FUNCTION(_Sorted.print) {
memo '_T5:4'
_Sorted.print:
    _T102 = 0
    _T101 = _T102
_L27:
    _T103 = *(_T5 + 8)
    _T104 = (_T101 < _T103)
    if (_T104 == 0) branch _L28
    _T105 = *(_T5 + 4)
    _T106 = *(_T105 + 0)
    _T107 = (_T101 < _T106)
    if (_T107 == 0) branch _L29
    _T108 = 0
    _T109 = (_T101 < _T108)
    if (_T109 == 0) branch _L30
_L29:
    _T110 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T110
    call _PrintString
    call _Halt
_L30:
    _T111 = 4
    _T112 = (_T101 * _T111)
    _T113 = (_T112 + _T111)
    _T114 = *(_T105 + _T113)
    parm _T114
    call _PrintInt
    _T115 = " "
    parm _T115
    call _PrintString
    _T116 = 1
    _T117 = (_T101 + _T116)
    _T101 = _T117
    branch _L27
_L28:
    _T118 = "\n"
    parm _T118
    call _PrintString
}

FUNCTION(_Sorted.merge) {
memo '_T6:4 _T7:8'
_Sorted.merge:
    _T120 = *(_T6 + 8)
    _T121 = *(_T7 + 8)
    _T122 = (_T120 + _T121)
    _T123 = 0
    _T124 = (_T122 < _T123)
    if (_T124 == 0) branch _L31
    _T125 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T125
    call _PrintString
    call _Halt
_L31:
    _T126 = 4
    _T127 = (_T126 * _T122)
    _T128 = (_T126 + _T127)
    parm _T128
    _T129 =  call _Alloc
    *(_T129 + 0) = _T122
    _T119 = _T129
    _T132 = 0
    _T130 = _T132
    _T133 = 0
    _T131 = _T133
_L32:
    _T134 = (_T130 + _T131)
    _T135 = *(_T6 + 8)
    _T136 = *(_T7 + 8)
    _T137 = (_T135 + _T136)
    _T138 = (_T134 < _T137)
    if (_T138 == 0) branch _L33
    _T139 = *(_T6 + 8)
    _T140 = (_T130 == _T139)
    if (_T140 == 0) branch _L34
    _T141 = *(_T7 + 4)
    _T142 = *(_T141 + 0)
    _T143 = (_T131 < _T142)
    if (_T143 == 0) branch _L35
    _T144 = 0
    _T145 = (_T131 < _T144)
    if (_T145 == 0) branch _L36
_L35:
    _T146 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T146
    call _PrintString
    call _Halt
_L36:
    _T147 = 4
    _T148 = (_T131 * _T147)
    _T149 = (_T148 + _T147)
    _T150 = *(_T141 + _T149)
    _T151 = (_T130 + _T131)
    _T152 = *(_T119 + 0)
    _T153 = (_T151 < _T152)
    if (_T153 == 0) branch _L37
    _T154 = 0
    _T155 = (_T151 < _T154)
    if (_T155 == 0) branch _L38
_L37:
    _T156 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T156
    call _PrintString
    call _Halt
_L38:
    _T157 = 4
    _T158 = (_T151 * _T157)
    _T159 = (_T158 + _T157)
    _T160 = *(_T119 + _T159)
    _T161 = 4
    _T162 = (_T151 * _T161)
    _T163 = (_T162 + _T161)
    *(_T119 + _T163) = _T150
    _T164 = 1
    _T165 = (_T131 + _T164)
    _T131 = _T165
    branch _L39
_L34:
    _T166 = *(_T7 + 8)
    _T167 = (_T131 == _T166)
    if (_T167 == 0) branch _L40
    _T168 = *(_T6 + 4)
    _T169 = *(_T168 + 0)
    _T170 = (_T130 < _T169)
    if (_T170 == 0) branch _L41
    _T171 = 0
    _T172 = (_T130 < _T171)
    if (_T172 == 0) branch _L42
_L41:
    _T173 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T173
    call _PrintString
    call _Halt
_L42:
    _T174 = 4
    _T175 = (_T130 * _T174)
    _T176 = (_T175 + _T174)
    _T177 = *(_T168 + _T176)
    _T178 = (_T130 + _T131)
    _T179 = *(_T119 + 0)
    _T180 = (_T178 < _T179)
    if (_T180 == 0) branch _L43
    _T181 = 0
    _T182 = (_T178 < _T181)
    if (_T182 == 0) branch _L44
_L43:
    _T183 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T183
    call _PrintString
    call _Halt
_L44:
    _T184 = 4
    _T185 = (_T178 * _T184)
    _T186 = (_T185 + _T184)
    _T187 = *(_T119 + _T186)
    _T188 = 4
    _T189 = (_T178 * _T188)
    _T190 = (_T189 + _T188)
    *(_T119 + _T190) = _T177
    _T191 = 1
    _T192 = (_T130 + _T191)
    _T130 = _T192
    branch _L45
_L40:
    _T193 = *(_T6 + 4)
    _T194 = *(_T193 + 0)
    _T195 = (_T130 < _T194)
    if (_T195 == 0) branch _L46
    _T196 = 0
    _T197 = (_T130 < _T196)
    if (_T197 == 0) branch _L47
_L46:
    _T198 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T198
    call _PrintString
    call _Halt
_L47:
    _T199 = 4
    _T200 = (_T130 * _T199)
    _T201 = (_T200 + _T199)
    _T202 = *(_T193 + _T201)
    _T203 = *(_T7 + 4)
    _T204 = *(_T203 + 0)
    _T205 = (_T131 < _T204)
    if (_T205 == 0) branch _L48
    _T206 = 0
    _T207 = (_T131 < _T206)
    if (_T207 == 0) branch _L49
_L48:
    _T208 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T208
    call _PrintString
    call _Halt
_L49:
    _T209 = 4
    _T210 = (_T131 * _T209)
    _T211 = (_T210 + _T209)
    _T212 = *(_T203 + _T211)
    _T213 = (_T202 < _T212)
    if (_T213 == 0) branch _L50
    _T214 = *(_T7 + 4)
    _T215 = *(_T214 + 0)
    _T216 = (_T131 < _T215)
    if (_T216 == 0) branch _L51
    _T217 = 0
    _T218 = (_T131 < _T217)
    if (_T218 == 0) branch _L52
_L51:
    _T219 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T219
    call _PrintString
    call _Halt
_L52:
    _T220 = 4
    _T221 = (_T131 * _T220)
    _T222 = (_T221 + _T220)
    _T223 = *(_T214 + _T222)
    _T224 = (_T130 + _T131)
    _T225 = *(_T119 + 0)
    _T226 = (_T224 < _T225)
    if (_T226 == 0) branch _L53
    _T227 = 0
    _T228 = (_T224 < _T227)
    if (_T228 == 0) branch _L54
_L53:
    _T229 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T229
    call _PrintString
    call _Halt
_L54:
    _T230 = 4
    _T231 = (_T224 * _T230)
    _T232 = (_T231 + _T230)
    _T233 = *(_T119 + _T232)
    _T234 = 4
    _T235 = (_T224 * _T234)
    _T236 = (_T235 + _T234)
    *(_T119 + _T236) = _T223
    _T237 = 1
    _T238 = (_T131 + _T237)
    _T131 = _T238
    branch _L55
_L50:
    _T239 = *(_T6 + 4)
    _T240 = *(_T239 + 0)
    _T241 = (_T130 < _T240)
    if (_T241 == 0) branch _L56
    _T242 = 0
    _T243 = (_T130 < _T242)
    if (_T243 == 0) branch _L57
_L56:
    _T244 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T244
    call _PrintString
    call _Halt
_L57:
    _T245 = 4
    _T246 = (_T130 * _T245)
    _T247 = (_T246 + _T245)
    _T248 = *(_T239 + _T247)
    _T249 = (_T130 + _T131)
    _T250 = *(_T119 + 0)
    _T251 = (_T249 < _T250)
    if (_T251 == 0) branch _L58
    _T252 = 0
    _T253 = (_T249 < _T252)
    if (_T253 == 0) branch _L59
_L58:
    _T254 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T254
    call _PrintString
    call _Halt
_L59:
    _T255 = 4
    _T256 = (_T249 * _T255)
    _T257 = (_T256 + _T255)
    _T258 = *(_T119 + _T257)
    _T259 = 4
    _T260 = (_T249 * _T259)
    _T261 = (_T260 + _T259)
    *(_T119 + _T261) = _T248
    _T262 = 1
    _T263 = (_T130 + _T262)
    _T130 = _T263
_L55:
_L45:
_L39:
    branch _L32
_L33:
    _T264 = *(_T6 + 4)
    *(_T6 + 4) = _T119
    _T265 = *(_T6 + 8)
    _T266 = *(_T7 + 8)
    _T267 = (_T265 + _T266)
    _T268 = *(_T6 + 8)
    *(_T6 + 8) = _T267
}

