package main

import (
	"os"
	"testing"
)

func TestParseXMLFile(t *testing.T) {
	xmlContent := `<config><var name="VAR1">value1</var><var name="VAR2">value2</var></config>`
	tmpFile, err := os.CreateTemp("", "testXML.xml")
	if err != nil {
		t.Fatal(err)
	}
	defer os.Remove(tmpFile.Name())

	if _, err := tmpFile.Write([]byte(xmlContent)); err != nil {
		t.Fatal(err)
	}
	tmpFile.Close()

	config, err := parseXMLFile(tmpFile.Name())
	if err != nil {
		t.Fatalf("[ Expected no error, got %v ]", err)
	}
	if len(config.Vars) != 2 {
		t.Fatalf("[ Expected 2 vars, got %d ]", len(config.Vars))
	}
	if config.Vars[0].Name != "VAR1" || config.Vars[0].Value != "value1" {
		t.Fatalf(`[ Expected var "VAR1" with value "value1", got "%s" with value "%s" ]`, config.Vars[0].Name, config.Vars[0].Value)
	}
}

func TestEvaluateConstants(t *testing.T) {
	variables := map[string]string{
		"VAR1": "value1",
		"VAR2": "value2",
	}

	result, err := evaluateConstants("Some value: !{VAR1}, undefined var: !{VAR3}", variables)
	if err != nil {
		t.Fatalf("[ Expected no error, got %v ]", err)
	}

	expected := "Some value: value1, undefined var: [undefined_var_VAR3 ]"
	if result != expected {
		t.Fatalf("[ Expected: %s \nGot: %s ]", expected, result)
	}
}

func TestConvertToConfigLang(t *testing.T) {
	config := &Config{
		Vars: []Var{
			{Name: "VAR1", Value: "value1"},
			{Name: "VAR2", Value: "Some config with !{VAR1}"},
		},
	}
	result, err := convertToConfigLang(config)
	if err != nil {
		t.Fatalf("Expected no error, got %v", err)
	}

	expected := "var VAR1 value1\nvar VAR2 Some config with value1\n"
	if result != expected {
		t.Fatalf("Expected '%s', got '%s'", expected, result)
	}
}
