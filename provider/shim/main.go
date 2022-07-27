package shim

import (
	"github.com/chainguard-dev/terraform-provider-ko/internal/provider"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/schema"
)

func NewProvider() *schema.Provider {
	return provider.New("")()
}
