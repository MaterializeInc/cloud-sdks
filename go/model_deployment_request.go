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
)

// DeploymentRequest struct for DeploymentRequest
type DeploymentRequest struct {
	Name *string `json:"name,omitempty"`
	CatalogRestoreMode *bool `json:"catalogRestoreMode,omitempty"`
	Size *DeploymentSizeEnum `json:"size,omitempty"`
	StorageMb *int32 `json:"storageMb,omitempty"`
	MaterializedExtraArgs *[]string `json:"materializedExtraArgs,omitempty"`
	MzVersion *string `json:"mzVersion,omitempty"`
	ReleaseTrack *ReleaseTrackEnum `json:"releaseTrack,omitempty"`
	EnableTailscale *bool `json:"enableTailscale,omitempty"`
	TailscaleAuthKey *string `json:"tailscaleAuthKey,omitempty"`
	CloudProviderRegion SupportedCloudRegionRequest `json:"cloudProviderRegion"`
}

// NewDeploymentRequest instantiates a new DeploymentRequest object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewDeploymentRequest(cloudProviderRegion SupportedCloudRegionRequest) *DeploymentRequest {
	this := DeploymentRequest{}
	var catalogRestoreMode bool = false
	this.CatalogRestoreMode = &catalogRestoreMode
	var storageMb int32 = 100
	this.StorageMb = &storageMb
	var enableTailscale bool = false
	this.EnableTailscale = &enableTailscale
	this.CloudProviderRegion = cloudProviderRegion
	return &this
}

// NewDeploymentRequestWithDefaults instantiates a new DeploymentRequest object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewDeploymentRequestWithDefaults() *DeploymentRequest {
	this := DeploymentRequest{}
	var catalogRestoreMode bool = false
	this.CatalogRestoreMode = &catalogRestoreMode
	var storageMb int32 = 100
	this.StorageMb = &storageMb
	var enableTailscale bool = false
	this.EnableTailscale = &enableTailscale
	return &this
}

// GetName returns the Name field value if set, zero value otherwise.
func (o *DeploymentRequest) GetName() string {
	if o == nil || o.Name == nil {
		var ret string
		return ret
	}
	return *o.Name
}

// GetNameOk returns a tuple with the Name field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *DeploymentRequest) GetNameOk() (*string, bool) {
	if o == nil || o.Name == nil {
		return nil, false
	}
	return o.Name, true
}

// HasName returns a boolean if a field has been set.
func (o *DeploymentRequest) HasName() bool {
	if o != nil && o.Name != nil {
		return true
	}

	return false
}

// SetName gets a reference to the given string and assigns it to the Name field.
func (o *DeploymentRequest) SetName(v string) {
	o.Name = &v
}

// GetCatalogRestoreMode returns the CatalogRestoreMode field value if set, zero value otherwise.
func (o *DeploymentRequest) GetCatalogRestoreMode() bool {
	if o == nil || o.CatalogRestoreMode == nil {
		var ret bool
		return ret
	}
	return *o.CatalogRestoreMode
}

// GetCatalogRestoreModeOk returns a tuple with the CatalogRestoreMode field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *DeploymentRequest) GetCatalogRestoreModeOk() (*bool, bool) {
	if o == nil || o.CatalogRestoreMode == nil {
		return nil, false
	}
	return o.CatalogRestoreMode, true
}

// HasCatalogRestoreMode returns a boolean if a field has been set.
func (o *DeploymentRequest) HasCatalogRestoreMode() bool {
	if o != nil && o.CatalogRestoreMode != nil {
		return true
	}

	return false
}

// SetCatalogRestoreMode gets a reference to the given bool and assigns it to the CatalogRestoreMode field.
func (o *DeploymentRequest) SetCatalogRestoreMode(v bool) {
	o.CatalogRestoreMode = &v
}

// GetSize returns the Size field value if set, zero value otherwise.
func (o *DeploymentRequest) GetSize() DeploymentSizeEnum {
	if o == nil || o.Size == nil {
		var ret DeploymentSizeEnum
		return ret
	}
	return *o.Size
}

// GetSizeOk returns a tuple with the Size field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *DeploymentRequest) GetSizeOk() (*DeploymentSizeEnum, bool) {
	if o == nil || o.Size == nil {
		return nil, false
	}
	return o.Size, true
}

// HasSize returns a boolean if a field has been set.
func (o *DeploymentRequest) HasSize() bool {
	if o != nil && o.Size != nil {
		return true
	}

	return false
}

// SetSize gets a reference to the given DeploymentSizeEnum and assigns it to the Size field.
func (o *DeploymentRequest) SetSize(v DeploymentSizeEnum) {
	o.Size = &v
}

// GetStorageMb returns the StorageMb field value if set, zero value otherwise.
func (o *DeploymentRequest) GetStorageMb() int32 {
	if o == nil || o.StorageMb == nil {
		var ret int32
		return ret
	}
	return *o.StorageMb
}

// GetStorageMbOk returns a tuple with the StorageMb field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *DeploymentRequest) GetStorageMbOk() (*int32, bool) {
	if o == nil || o.StorageMb == nil {
		return nil, false
	}
	return o.StorageMb, true
}

// HasStorageMb returns a boolean if a field has been set.
func (o *DeploymentRequest) HasStorageMb() bool {
	if o != nil && o.StorageMb != nil {
		return true
	}

	return false
}

// SetStorageMb gets a reference to the given int32 and assigns it to the StorageMb field.
func (o *DeploymentRequest) SetStorageMb(v int32) {
	o.StorageMb = &v
}

// GetMaterializedExtraArgs returns the MaterializedExtraArgs field value if set, zero value otherwise.
func (o *DeploymentRequest) GetMaterializedExtraArgs() []string {
	if o == nil || o.MaterializedExtraArgs == nil {
		var ret []string
		return ret
	}
	return *o.MaterializedExtraArgs
}

// GetMaterializedExtraArgsOk returns a tuple with the MaterializedExtraArgs field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *DeploymentRequest) GetMaterializedExtraArgsOk() (*[]string, bool) {
	if o == nil || o.MaterializedExtraArgs == nil {
		return nil, false
	}
	return o.MaterializedExtraArgs, true
}

// HasMaterializedExtraArgs returns a boolean if a field has been set.
func (o *DeploymentRequest) HasMaterializedExtraArgs() bool {
	if o != nil && o.MaterializedExtraArgs != nil {
		return true
	}

	return false
}

// SetMaterializedExtraArgs gets a reference to the given []string and assigns it to the MaterializedExtraArgs field.
func (o *DeploymentRequest) SetMaterializedExtraArgs(v []string) {
	o.MaterializedExtraArgs = &v
}

// GetMzVersion returns the MzVersion field value if set, zero value otherwise.
func (o *DeploymentRequest) GetMzVersion() string {
	if o == nil || o.MzVersion == nil {
		var ret string
		return ret
	}
	return *o.MzVersion
}

// GetMzVersionOk returns a tuple with the MzVersion field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *DeploymentRequest) GetMzVersionOk() (*string, bool) {
	if o == nil || o.MzVersion == nil {
		return nil, false
	}
	return o.MzVersion, true
}

// HasMzVersion returns a boolean if a field has been set.
func (o *DeploymentRequest) HasMzVersion() bool {
	if o != nil && o.MzVersion != nil {
		return true
	}

	return false
}

// SetMzVersion gets a reference to the given string and assigns it to the MzVersion field.
func (o *DeploymentRequest) SetMzVersion(v string) {
	o.MzVersion = &v
}

// GetReleaseTrack returns the ReleaseTrack field value if set, zero value otherwise.
func (o *DeploymentRequest) GetReleaseTrack() ReleaseTrackEnum {
	if o == nil || o.ReleaseTrack == nil {
		var ret ReleaseTrackEnum
		return ret
	}
	return *o.ReleaseTrack
}

// GetReleaseTrackOk returns a tuple with the ReleaseTrack field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *DeploymentRequest) GetReleaseTrackOk() (*ReleaseTrackEnum, bool) {
	if o == nil || o.ReleaseTrack == nil {
		return nil, false
	}
	return o.ReleaseTrack, true
}

// HasReleaseTrack returns a boolean if a field has been set.
func (o *DeploymentRequest) HasReleaseTrack() bool {
	if o != nil && o.ReleaseTrack != nil {
		return true
	}

	return false
}

// SetReleaseTrack gets a reference to the given ReleaseTrackEnum and assigns it to the ReleaseTrack field.
func (o *DeploymentRequest) SetReleaseTrack(v ReleaseTrackEnum) {
	o.ReleaseTrack = &v
}

// GetEnableTailscale returns the EnableTailscale field value if set, zero value otherwise.
func (o *DeploymentRequest) GetEnableTailscale() bool {
	if o == nil || o.EnableTailscale == nil {
		var ret bool
		return ret
	}
	return *o.EnableTailscale
}

// GetEnableTailscaleOk returns a tuple with the EnableTailscale field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *DeploymentRequest) GetEnableTailscaleOk() (*bool, bool) {
	if o == nil || o.EnableTailscale == nil {
		return nil, false
	}
	return o.EnableTailscale, true
}

// HasEnableTailscale returns a boolean if a field has been set.
func (o *DeploymentRequest) HasEnableTailscale() bool {
	if o != nil && o.EnableTailscale != nil {
		return true
	}

	return false
}

// SetEnableTailscale gets a reference to the given bool and assigns it to the EnableTailscale field.
func (o *DeploymentRequest) SetEnableTailscale(v bool) {
	o.EnableTailscale = &v
}

// GetTailscaleAuthKey returns the TailscaleAuthKey field value if set, zero value otherwise.
func (o *DeploymentRequest) GetTailscaleAuthKey() string {
	if o == nil || o.TailscaleAuthKey == nil {
		var ret string
		return ret
	}
	return *o.TailscaleAuthKey
}

// GetTailscaleAuthKeyOk returns a tuple with the TailscaleAuthKey field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *DeploymentRequest) GetTailscaleAuthKeyOk() (*string, bool) {
	if o == nil || o.TailscaleAuthKey == nil {
		return nil, false
	}
	return o.TailscaleAuthKey, true
}

// HasTailscaleAuthKey returns a boolean if a field has been set.
func (o *DeploymentRequest) HasTailscaleAuthKey() bool {
	if o != nil && o.TailscaleAuthKey != nil {
		return true
	}

	return false
}

// SetTailscaleAuthKey gets a reference to the given string and assigns it to the TailscaleAuthKey field.
func (o *DeploymentRequest) SetTailscaleAuthKey(v string) {
	o.TailscaleAuthKey = &v
}

// GetCloudProviderRegion returns the CloudProviderRegion field value
func (o *DeploymentRequest) GetCloudProviderRegion() SupportedCloudRegionRequest {
	if o == nil {
		var ret SupportedCloudRegionRequest
		return ret
	}

	return o.CloudProviderRegion
}

// GetCloudProviderRegionOk returns a tuple with the CloudProviderRegion field value
// and a boolean to check if the value has been set.
func (o *DeploymentRequest) GetCloudProviderRegionOk() (*SupportedCloudRegionRequest, bool) {
	if o == nil  {
		return nil, false
	}
	return &o.CloudProviderRegion, true
}

// SetCloudProviderRegion sets field value
func (o *DeploymentRequest) SetCloudProviderRegion(v SupportedCloudRegionRequest) {
	o.CloudProviderRegion = v
}

func (o DeploymentRequest) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if o.Name != nil {
		toSerialize["name"] = o.Name
	}
	if o.CatalogRestoreMode != nil {
		toSerialize["catalogRestoreMode"] = o.CatalogRestoreMode
	}
	if o.Size != nil {
		toSerialize["size"] = o.Size
	}
	if o.StorageMb != nil {
		toSerialize["storageMb"] = o.StorageMb
	}
	if o.MaterializedExtraArgs != nil {
		toSerialize["materializedExtraArgs"] = o.MaterializedExtraArgs
	}
	if o.MzVersion != nil {
		toSerialize["mzVersion"] = o.MzVersion
	}
	if o.ReleaseTrack != nil {
		toSerialize["releaseTrack"] = o.ReleaseTrack
	}
	if o.EnableTailscale != nil {
		toSerialize["enableTailscale"] = o.EnableTailscale
	}
	if o.TailscaleAuthKey != nil {
		toSerialize["tailscaleAuthKey"] = o.TailscaleAuthKey
	}
	if true {
		toSerialize["cloudProviderRegion"] = o.CloudProviderRegion
	}
	return json.Marshal(toSerialize)
}

type NullableDeploymentRequest struct {
	value *DeploymentRequest
	isSet bool
}

func (v NullableDeploymentRequest) Get() *DeploymentRequest {
	return v.value
}

func (v *NullableDeploymentRequest) Set(val *DeploymentRequest) {
	v.value = val
	v.isSet = true
}

func (v NullableDeploymentRequest) IsSet() bool {
	return v.isSet
}

func (v *NullableDeploymentRequest) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableDeploymentRequest(val *DeploymentRequest) *NullableDeploymentRequest {
	return &NullableDeploymentRequest{value: val, isSet: true}
}

func (v NullableDeploymentRequest) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableDeploymentRequest) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}


