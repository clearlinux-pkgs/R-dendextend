#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-dendextend
Version  : 1.7.0
Release  : 10
URL      : https://cran.r-project.org/src/contrib/dendextend_1.7.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/dendextend_1.7.0.tar.gz
Summary  : Extending 'dendrogram' Functionality in R
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-circlize
Requires: R-corrplot
Requires: R-gplots
BuildRequires : R-circlize
BuildRequires : R-corrplot
BuildRequires : R-fpc
BuildRequires : R-ggplot2
BuildRequires : R-gplots
BuildRequires : R-viridis
BuildRequires : R-whisker
BuildRequires : clr-R-helpers

%description
'dendrogram' objects in R, letting you visualize and compare trees of
    'hierarchical clusterings'. You can (1) Adjust a tree's graphical parameters
    - the color, size, type, etc of its branches, nodes and labels. (2)
    Visually and statistically compare different 'dendrograms' to one another.

%prep
%setup -q -c -n dendextend

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523299478

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523299478
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dendextend
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dendextend
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dendextend
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library dendextend|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/dendextend/CITATION
/usr/lib64/R/library/dendextend/DESCRIPTION
/usr/lib64/R/library/dendextend/INDEX
/usr/lib64/R/library/dendextend/Meta/Rd.rds
/usr/lib64/R/library/dendextend/Meta/data.rds
/usr/lib64/R/library/dendextend/Meta/demo.rds
/usr/lib64/R/library/dendextend/Meta/features.rds
/usr/lib64/R/library/dendextend/Meta/hsearch.rds
/usr/lib64/R/library/dendextend/Meta/links.rds
/usr/lib64/R/library/dendextend/Meta/nsInfo.rds
/usr/lib64/R/library/dendextend/Meta/package.rds
/usr/lib64/R/library/dendextend/Meta/vignette.rds
/usr/lib64/R/library/dendextend/NAMESPACE
/usr/lib64/R/library/dendextend/NEWS
/usr/lib64/R/library/dendextend/NEWS.md
/usr/lib64/R/library/dendextend/R/dendextend
/usr/lib64/R/library/dendextend/R/dendextend.rdb
/usr/lib64/R/library/dendextend/R/dendextend.rdx
/usr/lib64/R/library/dendextend/data/Rdata.rdb
/usr/lib64/R/library/dendextend/data/Rdata.rds
/usr/lib64/R/library/dendextend/data/Rdata.rdx
/usr/lib64/R/library/dendextend/demo/dendextend.R
/usr/lib64/R/library/dendextend/doc/Cluster_Analysis.R
/usr/lib64/R/library/dendextend/doc/Cluster_Analysis.Rmd
/usr/lib64/R/library/dendextend/doc/Cluster_Analysis.html
/usr/lib64/R/library/dendextend/doc/FAQ.R
/usr/lib64/R/library/dendextend/doc/FAQ.Rmd
/usr/lib64/R/library/dendextend/doc/FAQ.html
/usr/lib64/R/library/dendextend/doc/Quick_Introduction.R
/usr/lib64/R/library/dendextend/doc/Quick_Introduction.Rmd
/usr/lib64/R/library/dendextend/doc/Quick_Introduction.html
/usr/lib64/R/library/dendextend/doc/index.html
/usr/lib64/R/library/dendextend/doc/introduction.R
/usr/lib64/R/library/dendextend/doc/introduction.Rmd
/usr/lib64/R/library/dendextend/doc/introduction.html
/usr/lib64/R/library/dendextend/help/AnIndex
/usr/lib64/R/library/dendextend/help/aliases.rds
/usr/lib64/R/library/dendextend/help/dendextend.rdb
/usr/lib64/R/library/dendextend/help/dendextend.rdx
/usr/lib64/R/library/dendextend/help/paths.rds
/usr/lib64/R/library/dendextend/html/00Index.html
/usr/lib64/R/library/dendextend/html/R.css
