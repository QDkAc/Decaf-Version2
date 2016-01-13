VTABLE(_Main) {
    <empty>
    Main
}

VTABLE(_Item) {
    <empty>
    Item
    _Item.setId;
    _Item.printId;
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T3 = 4
    parm _T3
    _T4 =  call _Alloc
    _T5 = VTBL <_Main>
    *(_T4 + 0) = _T5
    return _T4
}

FUNCTION(_Item_New) {
memo ''
_Item_New:
    _T6 = 8
    parm _T6
    _T7 =  call _Alloc
    _T8 = 0
    *(_T7 + 4) = _T8
    _T9 = VTBL <_Item>
    *(_T7 + 0) = _T9
    return _T7
}

FUNCTION(main) {
memo ''
main:
    _T11 = 0
    _T10 = _T11
_L13:
    _T13 = 10
    _T14 = (_T10 < _T13)
    if (_T14 == 0) branch _L14
    _T15 =  call _Item_New
    _T12 = _T15
    parm _T12
    parm _T10
    _T16 = *(_T12 + 0)
    _T17 = *(_T16 + 8)
    call _T17
    parm _T12
    _T18 = *(_T12 + 0)
    _T19 = *(_T18 + 12)
    call _T19
    _T20 = 1
    _T21 = (_T10 + _T20)
    _T10 = _T21
    branch _L13
_L14:
}

FUNCTION(_Item.setId) {
memo '_T0:4 _T1:8'
_Item.setId:
    _T22 = *(_T0 + 4)
    *(_T0 + 4) = _T1
}

FUNCTION(_Item.printId) {
memo '_T2:4'
_Item.printId:
    _T23 = *(_T2 + 4)
    parm _T23
    call _PrintInt
    _T24 = "\n"
    parm _T24
    call _PrintString
}

