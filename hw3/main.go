package main

import (
	"encoding/xml"
	"fmt"
	"os"
	"regexp"
	"strings"
)

type Config struct {
	XMLName xml.Name `xml:"config"`
	Vars    []Var    `xml:"var"`
}

type Var struct {
	Name  string `xml:"name,attr"`
	Value string `xml:",chardata"`
}

func parseXMLFile(inputPath string) (*Config, error) {
	fileContent, err := os.ReadFile(inputPath)
	if err != nil {
		return nil, err
	}

	var config Config
	err = xml.Unmarshal(fileContent, &config)
	if err != nil {
		return nil, err
	}

	return &config, nil
}

func evaluateConstants(value string, variables map[string]string) (string, error) {
	re := regexp.MustCompile(`!\{([A-Za-z_][A-Za-z0-9_]*)\}`)

	return re.ReplaceAllStringFunc(value, func(match string) string {
		varName := re.FindStringSubmatch(match)[1]

		if val, ok := variables[varName]; ok {
			return val
		}

		return fmt.Sprintf(" [undefined_var_%s ]", varName)
	}), nil
}

func convertToConfigLang(config *Config) (string, error) {
	var result strings.Builder
	variables := make(map[string]string)
	for _, v := range config.Vars {
		cleanValue := strings.TrimSpace(v.Value)
		evaluatedValue, err := evaluateConstants(cleanValue, variables)

		if err != nil {
			return "", err
		}

		variables[v.Name] = evaluatedValue
		result.WriteString(fmt.Sprintf("var %s %s\n", v.Name, evaluatedValue))
	}
	return result.String(), nil
}

func main() {
	if len(os.Args) < 3 {
		fmt.Println("[ Usage: go run ./main.go <input XML file> <output file> ]")
		return
	}

	inputPath := os.Args[1]
	outputPath := os.Args[2]

	config, err := parseXMLFile(inputPath)
	if err != nil {
		fmt.Println("[ Error parsing XML:", err, "]")
	}

	outputContent, err := convertToConfigLang(config)
	if err != nil {
		fmt.Println("[ Error while converting:", err, "]")
		return
	}

	err = os.WriteFile(outputPath, []byte(outputContent), 0644)
	if err != nil {
		fmt.Println("[ Error writing output file:", err, "]")
	}

	fmt.Println("[ Success! ]")
}
