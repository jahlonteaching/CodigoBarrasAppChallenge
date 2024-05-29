import inspect

import pytest

import app.model.barcode

module_members = [item[0] for item in inspect.getmembers(app.model.barcode)]
BarCodeValidator_class_defined = 'BarCodeValidator' in module_members
LengthValidator_class_defined = 'LengthValidator' in module_members
CountryCodeValidator_class_defined = 'CountryCodeValidator' in module_members
ProductCodeValidator_class_defined = 'ProductCodeValidator' in module_members
ControlDigitValidator_class_defined = 'ControlDigitValidator' in module_members
BarCode_class_defined = 'BarCode' in module_members

if BarCodeValidator_class_defined:
    from app.model.barcode import BarCodeValidator

if LengthValidator_class_defined:
    from app.model.barcode import LengthValidator

if CountryCodeValidator_class_defined:
    from app.model.barcode import CountryCodeValidator

if ProductCodeValidator_class_defined:
    from app.model.barcode import ProductCodeValidator

if ControlDigitValidator_class_defined:
    from app.model.barcode import ControlDigitValidator

if BarCode_class_defined:
    from app.model.barcode import BarCode


@pytest.fixture(scope="session")
def module_members_types():
    return {item[0]: item[1] for item in inspect.getmembers(app.model.barcode)}


def test_module_has_BarCodeValidator_class():
    assert BarCodeValidator_class_defined, "BarCodeValidator class not defined"


@pytest.mark.xfail(not BarCodeValidator_class_defined, reason="BarCodeValidator class not defined")
def test_BarCodeValidator_class_is_abstract(module_members_types):
    assert inspect.isabstract(module_members_types["BarCodeValidator"]), "BarCodeValidator class is not abstract"


@pytest.mark.xfail(not BarCodeValidator_class_defined, reason="BarCodeValidator class not defined")
def test_BarCodeValidator_class_has_check_method(module_members_types):
    assert "check" in module_members_types["BarCodeValidator"].__dict__, "BarCodeValidator class has no check method"


@pytest.mark.xfail(not BarCodeValidator_class_defined, reason="BarCodeValidator class not defined")
def test_BarCodeValidator_class_check_method_is_abstract(module_members_types):
    assert hasattr(module_members_types["BarCodeValidator"].check, "__isabstractmethod__"), \
        "BarCodeValidator check method is not abstract"


def test_module_has_LengthValidator_class():
    assert LengthValidator_class_defined, "LengthValidator class not defined"


@pytest.mark.xfail(not LengthValidator_class_defined, reason="LengthValidator class not defined")
def test_LengthValidator_class_inherits_BarCodeValidator(module_members_types):
    assert issubclass(module_members_types["LengthValidator"], module_members_types["BarCodeValidator"]), \
        "LengthValidator class does not inherit from BarCodeValidator"


@pytest.mark.xfail(not LengthValidator_class_defined, reason="LengthValidator class not defined")
def test_LengthValidator_class_has_check_method(module_members_types):
    assert "check" in module_members_types["LengthValidator"].__dict__, "LengthValidator class has no check method"


@pytest.mark.xfail(not LengthValidator_class_defined, reason="LengthValidator class not defined")
@pytest.mark.parametrize("code, expected", [("1234567890123456", True), ("123456789012345", False)])
def test_LengthValidator_class_check_method_returns_expected_result(module_members_types, code, expected):
    assert module_members_types["LengthValidator"]().check(code) == expected


def test_module_has_CountryCodeValidator_class():
    assert CountryCodeValidator_class_defined, "CountryCodeValidator class not defined"


@pytest.mark.xfail(not CountryCodeValidator_class_defined, reason="CountryCodeValidator class not defined")
def test_CountryCodeValidator_class_inherits_BarCodeValidator(module_members_types):
    assert issubclass(module_members_types["CountryCodeValidator"], module_members_types["BarCodeValidator"]), \
        "CountryCodeValidator class does not inherit from BarCodeValidator"


@pytest.mark.xfail(not CountryCodeValidator_class_defined, reason="CountryCodeValidator class not defined")
def test_CountryCodeValidator_class_has_check_method(module_members_types):
    assert "check" in module_members_types["CountryCodeValidator"].__dict__, \
        "CountryCodeValidator class has no check method"


@pytest.mark.xfail(not CountryCodeValidator_class_defined, reason="CountryCodeValidator class not defined")
@pytest.mark.parametrize("code, expected",
                         [("ABC4567890123456", True),
                          ("1234567890123456", False),
                          ("AB34567890123456", False),
                          ("", False),
                          ("AB", False)])
def test_CountryCodeValidator_class_check_method_returns_expected_result(module_members_types, code, expected):
    assert module_members_types["CountryCodeValidator"]().check(code) == expected


def test_module_has_ProductCodeValidator_class():
    assert ProductCodeValidator_class_defined, "ProductCodeValidator class not defined"


@pytest.mark.xfail(not ProductCodeValidator_class_defined, reason="ProductCodeValidator class not defined")
def test_ProductCodeValidator_class_inherits_BarCodeValidator(module_members_types):
    assert issubclass(module_members_types["ProductCodeValidator"], module_members_types["BarCodeValidator"]), \
        "ProductCodeValidator class does not inherit from BarCodeValidator"


@pytest.mark.xfail(not ProductCodeValidator_class_defined, reason="ProductCodeValidator class not defined")
def test_ProductCodeValidator_class_has_check_method(module_members_types):
    assert "check" in module_members_types["ProductCodeValidator"].__dict__, \
        "ProductCodeValidator class has no check method"


@pytest.mark.xfail(not ProductCodeValidator_class_defined, reason="ProductCodeValidator class not defined")
@pytest.mark.parametrize("code, expected",
                         [("ABC4567890123456", True),
                          ("123456789", False),
                          ("ABC456789012345A", False),
                          ("", False),
                          ("AB", False)])
def test_ProductCodeValidator_class_check_method_returns_expected_result(module_members_types, code, expected):
    assert module_members_types["ProductCodeValidator"]().check(code) == expected


def test_module_has_ControlDigitValidator_class():
    assert ControlDigitValidator_class_defined, "ControlDigitValidator class not defined"


@pytest.mark.xfail(not ControlDigitValidator_class_defined, reason="ControlDigitValidator class not defined")
def test_ControlDigitValidator_class_inherits_BarCodeValidator(module_members_types):
    assert issubclass(module_members_types["ControlDigitValidator"], module_members_types["BarCodeValidator"]), \
        "ControlDigitValidator class does not inherit from BarCodeValidator"


@pytest.mark.xfail(not ControlDigitValidator_class_defined, reason="ControlDigitValidator class not defined")
def test_ControlDigitValidator_class_has_check_method(module_members_types):
    assert "check" in module_members_types["ControlDigitValidator"].__dict__, \
        "ControlDigitValidator class has no check method"


@pytest.mark.xfail(not ControlDigitValidator_class_defined, reason="ControlDigitValidator class not defined")
def test_ControlDigitValidator_class_has_calculate_control_digit_method(module_members_types):
    assert "calculate_control_digit" in module_members_types["ControlDigitValidator"].__dict__, \
        "ControlDigitValidator class has no calculate_control_digit method"


@pytest.mark.xfail(not ControlDigitValidator_class_defined, reason="ControlDigitValidator class not defined")
@pytest.mark.parametrize("code, expected",
                         [("ABC4567890123458", 8),
                          ("XYZ8476923783669", 9),
                          ("AAA1111111111116", 6),
                          ("ZZZ9999999999994", 4),
                          ("AAA1000000000007", 7),
                          ("AAA0000000000019", 9),])
def test_ControlDigitValidator_class_calculate_control_digit_method_returns_expected_result(module_members_types, code,                                                                   expected):
    assert module_members_types["ControlDigitValidator"].calculate_control_digit(code) == expected


@pytest.mark.xfail(not ControlDigitValidator_class_defined, reason="ControlDigitValidator class not defined")
@pytest.mark.parametrize("code, expected",
                         [("ABC4567890123458", True),
                          ("XYZ8476923783669", True),
                          ("AAA1111111111116", True),
                          ("ZZZ9999999999994", True),
                          ("AAA1000000000007", True),
                          ("ABC4567890123456", False),
                          ("XYZ8476923783668", False),
                          ("", False),
                          ("AB", False)])
def test_ControlDigitValidator_class_check_method_returns_expected_result(module_members_types, code, expected):
    assert module_members_types["ControlDigitValidator"]().check(code) == expected


def test_module_has_BarCode_class():
    assert BarCode_class_defined, "BarCode class not defined"


@pytest.mark.xfail(not BarCode_class_defined, reason="BarCode class not defined")
def test_BarCode_class_has_validate_method(module_members_types):
    assert "validate" in module_members_types["BarCode"].__dict__, "BarCode class has no validate method"


@pytest.mark.xfail(not BarCode_class_defined, reason="BarCode class not defined")
def test_BarCode_class_has_code_attribute(module_members_types):
    assert "code" in dir(module_members_types["BarCode"]("ABC1234567890123")), "BarCode class has no code attribute"


@pytest.mark.xfail(not BarCode_class_defined, reason="BarCode class not defined")
def test_BarCode_class_has_validators_attribute(module_members_types):
    assert "validators" in dir(module_members_types["BarCode"]("ABC1234567890123")), "BarCode class has no validators attribute"


@pytest.mark.xfail(not BarCode_class_defined, reason="BarCode class not defined")
def test_BarCode_class_initializes_code_attribute(module_members_types):
    assert module_members_types["BarCode"]("ABC1234567890123").code == "ABC1234567890123", \
        "BarCode class does not initialize code attribute correctly"


@pytest.mark.xfail(not BarCode_class_defined, reason="BarCode class not defined")
def test_BarCode_class_initializes_validators_attribute(module_members_types):
    validators = module_members_types["BarCode"]("ABC1234567890123").validators
    assert len(validators) == 4, "BarCode class does not initialize validators attribute correctly"
    assert validators[0].__class__.__name__ == "LengthValidator", "BarCode class does not initialize validators attribute correctly"
    assert validators[1].__class__.__name__ == "CountryCodeValidator", "BarCode class does not initialize validators attribute correctly"
    assert validators[2].__class__.__name__ == "ProductCodeValidator", "BarCode class does not initialize validators attribute correctly"
    assert validators[3].__class__.__name__ == "ControlDigitValidator", "BarCode class does not initialize validators attribute correctly"


@pytest.mark.xfail(not BarCode_class_defined, reason="BarCode class not defined")
@pytest.mark.parametrize("code, error",
                         [("ABC123456789", "InvalidCodeStructureError"),
                          ("X3Z8476923783669", "InvalidCodeStructureError"),
                          ("AAA10AB000000007", "InvalidCodeStructureError"),
                          ("AAA1111111111111", "InvalidControlDigitError")])
def test_BarCode_class_validate_method_raises_error_when_code_is_invalid(module_members_types, code, error):
    with pytest.raises(module_members_types[error]):
        module_members_types["BarCode"](code).validate()


@pytest.mark.xfail(not BarCode_class_defined, reason="BarCode class not defined")
def test_BarCode_class_validate_method_does_not_raise_error_when_code_is_valid(module_members_types):
    try:
        module_members_types["BarCode"]("XYZ8476923783669").validate()
    except (module_members_types["InvalidCodeStructureError"], module_members_types["InvalidControlDigitError"]):
        pytest.fail("BarCode class raises an error when the code is valid")


@pytest.mark.xfail(not BarCode_class_defined, reason="BarCode class not defined")
def test_BarCode_class_validate_method_returns_true_when_code_is_valid(module_members_types):
    assert module_members_types["BarCode"]("XYZ8476923783669").validate(), \
        "BarCode class validate method returns False when the code is valid"
