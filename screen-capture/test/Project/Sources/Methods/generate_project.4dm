//%attributes = {}
$params:=New object:C1471
$params.PRODUCT_NAME:="screen-capture"
$params.PRODUCT_VERSION:="2.1.0"
$params.AUTHOR:="miyako"
$params.CREATE_DATE:=Current date:C33
$params.COPYRIGHT_YEAR:=Year of:C25(Current date:C33)

generate_project_source ($params)
generate_project_vs ($params)
generate_project_xcode ($params)
generate_project_plugin_stub ($params)