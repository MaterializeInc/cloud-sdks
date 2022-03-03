/*
 * Materialize Cloud
 *
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * API version: 0.1.0
 */

// Code generated by OpenAPI Generator (https://openapi-generator.tech); DO NOT EDIT.

package mzcloud

import (
	"encoding/json"
	"fmt"
)

// ReleaseTrackEnum the model 'ReleaseTrackEnum'
type ReleaseTrackEnum string

// List of ReleaseTrackEnum
const (
	CANARY ReleaseTrackEnum = "canary"
	STABLE ReleaseTrackEnum = "stable"
)

var allowedReleaseTrackEnumEnumValues = []ReleaseTrackEnum{
	"canary",
	"stable",
}

func (v *ReleaseTrackEnum) UnmarshalJSON(src []byte) error {
	var value string
	err := json.Unmarshal(src, &value)
	if err != nil {
		return err
	}
	enumTypeValue := ReleaseTrackEnum(value)
	for _, existing := range allowedReleaseTrackEnumEnumValues {
		if existing == enumTypeValue {
			*v = enumTypeValue
			return nil
		}
	}

	return fmt.Errorf("%+v is not a valid ReleaseTrackEnum", value)
}

// NewReleaseTrackEnumFromValue returns a pointer to a valid ReleaseTrackEnum
// for the value passed as argument, or an error if the value passed is not allowed by the enum
func NewReleaseTrackEnumFromValue(v string) (*ReleaseTrackEnum, error) {
	ev := ReleaseTrackEnum(v)
	if ev.IsValid() {
		return &ev, nil
	} else {
		return nil, fmt.Errorf("invalid value '%v' for ReleaseTrackEnum: valid values are %v", v, allowedReleaseTrackEnumEnumValues)
	}
}

// IsValid return true if the value is valid for the enum, false otherwise
func (v ReleaseTrackEnum) IsValid() bool {
	for _, existing := range allowedReleaseTrackEnumEnumValues {
		if existing == v {
			return true
		}
	}
	return false
}

// Ptr returns reference to ReleaseTrackEnum value
func (v ReleaseTrackEnum) Ptr() *ReleaseTrackEnum {
	return &v
}

type NullableReleaseTrackEnum struct {
	value *ReleaseTrackEnum
	isSet bool
}

func (v NullableReleaseTrackEnum) Get() *ReleaseTrackEnum {
	return v.value
}

func (v *NullableReleaseTrackEnum) Set(val *ReleaseTrackEnum) {
	v.value = val
	v.isSet = true
}

func (v NullableReleaseTrackEnum) IsSet() bool {
	return v.isSet
}

func (v *NullableReleaseTrackEnum) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableReleaseTrackEnum(val *ReleaseTrackEnum) *NullableReleaseTrackEnum {
	return &NullableReleaseTrackEnum{value: val, isSet: true}
}

func (v NullableReleaseTrackEnum) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableReleaseTrackEnum) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}

