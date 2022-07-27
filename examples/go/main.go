package main

import (
	"github.com/joshrwolf/pulumi-ko/sdk/go/ko"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		ki, err := ko.NewKoImage(ctx, "test", &ko.KoImageArgs{
			// This `importpath` is a neat and mostly useless byproduct of using go
			Importpath: pulumi.String("pulumi-ko-examples"),
		})
		if err != nil {
			return err
		}

		ctx.Export("digest", ki.ImageRef)

		return nil
	})
}
