#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-hms
Version  : 1.1.1
Release  : 66
URL      : https://cran.r-project.org/src/contrib/hms_1.1.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/hms_1.1.1.tar.gz
Summary  : Pretty Time of Day
Group    : Development/Tools
License  : MIT
Requires: R-ellipsis
Requires: R-lifecycle
Requires: R-pkgconfig
Requires: R-rlang
Requires: R-vctrs
BuildRequires : R-ellipsis
BuildRequires : R-lifecycle
BuildRequires : R-pkgconfig
BuildRequires : R-rlang
BuildRequires : R-vctrs
BuildRequires : buildreq-R

%description
values, based on the 'difftime' class.

%prep
%setup -q -c -n hms
cd %{_builddir}/hms

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641033217

%install
export SOURCE_DATE_EPOCH=1641033217
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library hms
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library hms
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library hms
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc hms || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/hms/DESCRIPTION
/usr/lib64/R/library/hms/INDEX
/usr/lib64/R/library/hms/LICENSE
/usr/lib64/R/library/hms/Meta/Rd.rds
/usr/lib64/R/library/hms/Meta/features.rds
/usr/lib64/R/library/hms/Meta/hsearch.rds
/usr/lib64/R/library/hms/Meta/links.rds
/usr/lib64/R/library/hms/Meta/nsInfo.rds
/usr/lib64/R/library/hms/Meta/package.rds
/usr/lib64/R/library/hms/NAMESPACE
/usr/lib64/R/library/hms/NEWS.md
/usr/lib64/R/library/hms/R/hms
/usr/lib64/R/library/hms/R/hms.rdb
/usr/lib64/R/library/hms/R/hms.rdx
/usr/lib64/R/library/hms/help/AnIndex
/usr/lib64/R/library/hms/help/aliases.rds
/usr/lib64/R/library/hms/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/hms/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/hms/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/hms/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/hms/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/hms/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/hms/help/figures/lifecycle-soft-deprecated.svg
/usr/lib64/R/library/hms/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/hms/help/figures/logo.png
/usr/lib64/R/library/hms/help/hms.rdb
/usr/lib64/R/library/hms/help/hms.rdx
/usr/lib64/R/library/hms/help/paths.rds
/usr/lib64/R/library/hms/html/00Index.html
/usr/lib64/R/library/hms/html/R.css
/usr/lib64/R/library/hms/tests/testthat.R
/usr/lib64/R/library/hms/tests/testthat/_snaps/colformat.md
/usr/lib64/R/library/hms/tests/testthat/helper-compare.R
/usr/lib64/R/library/hms/tests/testthat/test-arith.R
/usr/lib64/R/library/hms/tests/testthat/test-coercion-deprecated.R
/usr/lib64/R/library/hms/tests/testthat/test-coercion.R
/usr/lib64/R/library/hms/tests/testthat/test-colformat.R
/usr/lib64/R/library/hms/tests/testthat/test-combine.R
/usr/lib64/R/library/hms/tests/testthat/test-construct.R
/usr/lib64/R/library/hms/tests/testthat/test-lubridate.R
/usr/lib64/R/library/hms/tests/testthat/test-output.R
/usr/lib64/R/library/hms/tests/testthat/test-parse.R
/usr/lib64/R/library/hms/tests/testthat/test-round.R
/usr/lib64/R/library/hms/tests/testthat/test-subset.R
/usr/lib64/R/library/hms/tests/testthat/test-unique.R
/usr/lib64/R/library/hms/tests/testthat/test-update.R
