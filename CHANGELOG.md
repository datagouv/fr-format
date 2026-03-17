# Changelog

## 0.5.0 (2026-03-17)
- **refactor!: Remove specialized new method for INSEE geographical formats ([#41](https://github.com/datagouv/fr-format/pull/41))**
  # Goal
  
  The goal of this PR is to remove the specific `new_geo` method (used
  exclusively to create INSEE geo formats), and handle all `VersionedSet`
  instances within a single class `VersionedSetFormat`.
  
  BREAKING CHANGE: the validators formerly named `cog` parameter is
  replaced with `version`. Its expected value is unchanged, only the name
  changes.
  
  ---------
  
  Co-authored-by: Pierre Camilleri <pierre.camilleri@multi.coop>
- Add new `IdRNB` format ([#54](https://github.com/datagouv/fr-format/pull/54))
- All doc in French ([#55](https://github.com/datagouv/fr-format/pull/55))
- Automatic pyproject.toml version Bump (v0.4.1) [skip ci]
- Docs: Add contribution file to the project ([#38](https://github.com/datagouv/fr-format/pull/38))
- Docs: Improve README file with more details ([#40](https://github.com/datagouv/fr-format/pull/40))
- Feat: Get all valid values set ([#42](https://github.com/datagouv/fr-format/pull/42))
- Feat: Improve CodeRegion and Region formats with new versions. ([#46](https://github.com/datagouv/fr-format/pull/46))
- Feat: Update the format code postal with reliable source ([#47](https://github.com/datagouv/fr-format/pull/47))
- Fix paths to files in docs ([#52](https://github.com/datagouv/fr-format/pull/52))
- Fix remaining issues in docs and modernize codebase (python >= 3.10) ([#53](https://github.com/datagouv/fr-format/pull/53))
- Make structure consistent with our other repos ([#51](https://github.com/datagouv/fr-format/pull/51))
- Rationalize imports ([#57](https://github.com/datagouv/fr-format/pull/57))
- Refactor: Add a forgotten line break ([#44](https://github.com/datagouv/fr-format/pull/44))
- Refactor: factorize enum and geo format ([#37](https://github.com/datagouv/fr-format/pull/37))
- Rename `NumeroDepartement` to `CodeDepartement` ([#56](https://github.com/datagouv/fr-format/pull/56))
- feat: Display the source of each French format ([#43](https://github.com/datagouv/fr-format/pull/43))


Adding validation functionality :

- Code pays
- Pays
- Canton
- Code fantoir
- Code région
- Région
- Numero département
- Departement
- Code postal
- Code commune INSEE
- Commune 

Introduce validation option "strict" vs "lenient" that allows to be more or 
less strict on case and special characters.
