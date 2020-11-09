import pytest

from openapi_parser.enumeration import *

data_type_provider = (
    ("integer", DataType.INTEGER),
    ("number", DataType.NUMBER),
    ("string", DataType.STRING),
    ("boolean", DataType.BOOLEAN),
    ("array", DataType.ARRAY),
    ("object", DataType.OBJECT),
)


@pytest.mark.parametrize(['string_value', 'expected'], data_type_provider)
def test_data_type(string_value: str, expected: DataType):
    assert DataType(string_value) == expected


def test_data_type_error():
    with pytest.raises(ValueError):
        DataType("invalid")


integer_format_provider = (
    ("int32", IntegerFormat.INT32),
    ("int64", IntegerFormat.INT64),
)


@pytest.mark.parametrize(['string_value', 'expected'], integer_format_provider)
def test_integer_format(string_value: str, expected: IntegerFormat):
    assert IntegerFormat(string_value) == expected


def test_integer_format_error():
    with pytest.raises(ValueError):
        IntegerFormat("invalid")


number_format_provider = (
    ("float", NumberFormat.FLOAT),
    ("double", NumberFormat.DOUBLE),
)


@pytest.mark.parametrize(['string_value', 'expected'], number_format_provider)
def test_number_format(string_value: str, expected: NumberFormat):
    assert NumberFormat(string_value) == expected


def test_number_format_error():
    with pytest.raises(ValueError):
        NumberFormat("invalid")


string_format_provider = (
    ("byte", StringFormat.BYTE),
    ("binary", StringFormat.BINARY),
    ("date", StringFormat.DATE),
    ("date-time", StringFormat.DATETIME),
    ("password", StringFormat.PASSWORD),
    ("uuid", StringFormat.UUID),
    ("email", StringFormat.EMAIL),
)


@pytest.mark.parametrize(['string_value', 'expected'], string_format_provider)
def test_string_format(string_value: str, expected: StringFormat):
    assert StringFormat(string_value) == expected


def test_string_format_error():
    with pytest.raises(ValueError):
        StringFormat("invalid")


operation_method_provider = (
    ("get", OperationMethod.GET),
    ("put", OperationMethod.PUT),
    ("post", OperationMethod.POST),
    ("delete", OperationMethod.DELETE),
    ("options", OperationMethod.OPTIONS),
    ("head", OperationMethod.HEAD),
    ("patch", OperationMethod.PATCH),
    ("trace", OperationMethod.TRACE),
)


@pytest.mark.parametrize(['string_value', 'expected'], operation_method_provider)
def test_operation_method(string_value: str, expected: OperationMethod):
    assert OperationMethod(string_value) == expected


def test_operation_method_error():
    with pytest.raises(ValueError):
        OperationMethod("invalid")


base_location_provider = (
    ("header", BaseLocation.HEADER),
    ("query", BaseLocation.QUERY),
    ("cookie", BaseLocation.COOKIE),
)


@pytest.mark.parametrize(['string_value', 'expected'], base_location_provider)
def test_base_location(string_value: str, expected: BaseLocation):
    assert BaseLocation(string_value) == expected


def test_base_location_error():
    with pytest.raises(ValueError):
        BaseLocation("invalid")


parameter_location_provider = (
    ("header", ParameterLocation.HEADER),
    ("query", ParameterLocation.QUERY),
    ("cookie", ParameterLocation.COOKIE),
    ("path", ParameterLocation.PATH),
)


@pytest.mark.parametrize(['string_value', 'expected'], parameter_location_provider)
def test_parameter_location(string_value: str, expected: ParameterLocation):
    assert ParameterLocation(string_value) == expected


def test_parameter_location_error():
    with pytest.raises(ValueError):
        ParameterLocation("invalid")


media_type_provider = (
    ("application/json", MediaType.JSON),
    ("application/xml", MediaType.XML),
    ("application/x-www-form-urlencoded", MediaType.FORM),
    ("multipart_form/form-data", MediaType.MULTIPART_FORM),
    ("text/plain; charset=utf-8", MediaType.PLAIN_TEXT),
    ("text/html", MediaType.HTML),
    ("application/pdf", MediaType.PDF),
    ("image/png", MediaType.PNG),
)


@pytest.mark.parametrize(['string_value', 'expected'], media_type_provider)
def test_media_type(string_value: str, expected: MediaType):
    assert MediaType(string_value) == expected


def test_media_type_error():
    with pytest.raises(ValueError):
        MediaType("invalid")


security_type_provider = (
    ("apiKey", SecurityType.API_KEY),
    ("http", SecurityType.HTTP),
    ("oauth2", SecurityType.OAUTH2),
    ("openIdConnect", SecurityType.OPEN_ID_CONNECT),
)


@pytest.mark.parametrize(['string_value', 'expected'], security_type_provider)
def test_security_type(string_value: str, expected: SecurityType):
    assert SecurityType(string_value) == expected


def test_security_type_error():
    with pytest.raises(ValueError):
        SecurityType("invalid")


auth_schema_provider = (
    ("Basic", AuthenticationScheme.BASIC),
    ("Bearer", AuthenticationScheme.BEARER),
    ("Digest", AuthenticationScheme.DIGEST),
    ("HOBA", AuthenticationScheme.HOBA),
    ("Mutual", AuthenticationScheme.MUTUAL),
    ("Negotiate", AuthenticationScheme.NEGOTIATE),
    ("OAuth", AuthenticationScheme.OAUTH),
    ("SCRAM-SHA-1", AuthenticationScheme.SCRAM_SHA1),
    ("SCRAM-SHA-256", AuthenticationScheme.SCRAM_SHA256),
    ("vapid", AuthenticationScheme.VAPID),
)


@pytest.mark.parametrize(['string_value', 'expected'], auth_schema_provider)
def test_auth_schema(string_value: str, expected: AuthenticationScheme):
    assert AuthenticationScheme(string_value) == expected


def test_auth_schema_error():
    with pytest.raises(ValueError):
        AuthenticationScheme("invalid")


auth_flow_provider = (
    ("implicit", OAuthFlowType.IMPLICIT),
    ("password", OAuthFlowType.PASSWORD),
    ("clientCredentials", OAuthFlowType.CLIENT_CREDENTIALS),
    ("authorizationCode", OAuthFlowType.AUTHORIZATION_CODE),
)


@pytest.mark.parametrize(['string_value', 'expected'], auth_flow_provider)
def test_auth_flow(string_value: str, expected: OAuthFlowType):
    assert OAuthFlowType(string_value) == expected


def test_auth_flow_error():
    with pytest.raises(ValueError):
        OAuthFlowType("invalid")
