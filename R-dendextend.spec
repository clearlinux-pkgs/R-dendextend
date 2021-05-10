#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-dendextend
Version  : 1.15.1
Release  : 48
URL      : https://cran.r-project.org/src/contrib/dendextend_1.15.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/dendextend_1.15.1.tar.gz
Summary  : Extending 'dendrogram' Functionality in R
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-circlize
Requires: R-corrplot
Requires: R-dynamicTreeCut
Requires: R-ggplot2
Requires: R-gplots
Requires: R-magrittr
Requires: R-pvclust
Requires: R-viridis
BuildRequires : R-circlize
BuildRequires : R-corrplot
BuildRequires : R-dynamicTreeCut
BuildRequires : R-fpc
BuildRequires : R-ggplot2
BuildRequires : R-gplots
BuildRequires : R-magrittr
BuildRequires : R-pvclust
BuildRequires : R-viridis
BuildRequires : R-whisker
BuildRequires : buildreq-R

%description
'dendrogram' objects in R, letting you visualize and compare trees of
    'hierarchical clusterings'. You can (1) Adjust a tree's graphical parameters
    - the color, size, type, etc of its branches, nodes and labels. (2)
    Visually and statistically compare different 'dendrograms' to one another.

%prep
%setup -q -c -n dendextend
cd %{_builddir}/dendextend

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1620660914

%install
export SOURCE_DATE_EPOCH=1620660914
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
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc dendextend || :


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
/usr/lib64/R/library/dendextend/WORDLIST
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
/usr/lib64/R/library/dendextend/doc/dendextend.R
/usr/lib64/R/library/dendextend/doc/dendextend.Rmd
/usr/lib64/R/library/dendextend/doc/dendextend.html
/usr/lib64/R/library/dendextend/doc/index.html
/usr/lib64/R/library/dendextend/help/AnIndex
/usr/lib64/R/library/dendextend/help/aliases.rds
/usr/lib64/R/library/dendextend/help/dendextend.rdb
/usr/lib64/R/library/dendextend/help/dendextend.rdx
/usr/lib64/R/library/dendextend/help/paths.rds
/usr/lib64/R/library/dendextend/html/00Index.html
/usr/lib64/R/library/dendextend/html/R.css
/usr/lib64/R/library/dendextend/tests/test-all.R
/usr/lib64/R/library/dendextend/tests/testthat/test-attr_access.R
/usr/lib64/R/library/dendextend/tests/testthat/test-bk_method.R
/usr/lib64/R/library/dendextend/tests/testthat/test-branches_attr_by.R
/usr/lib64/R/library/dendextend/tests/testthat/test-common_subtrees.R
/usr/lib64/R/library/dendextend/tests/testthat/test-cor_bakers_gamma.R
/usr/lib64/R/library/dendextend/tests/testthat/test-cor_cophenetic.R
/usr/lib64/R/library/dendextend/tests/testthat/test-cut_lower_fun.R
/usr/lib64/R/library/dendextend/tests/testthat/test-cutree.dendrogram.R
/usr/lib64/R/library/dendextend/tests/testthat/test-dendlist.R
/usr/lib64/R/library/dendextend/tests/testthat/test-distinct_edges.R
/usr/lib64/R/library/dendextend/tests/testthat/test-entanglement.R
/usr/lib64/R/library/dendextend/tests/testthat/test-find_dendrogram.R
/usr/lib64/R/library/dendextend/tests/testthat/test-general.R
/usr/lib64/R/library/dendextend/tests/testthat/test-get_subdendrograms.R
/usr/lib64/R/library/dendextend/tests/testthat/test-ggdend.R
/usr/lib64/R/library/dendextend/tests/testthat/test-highlight_branches.R
/usr/lib64/R/library/dendextend/tests/testthat/test-labels-assign.R
/usr/lib64/R/library/dendextend/tests/testthat/test-labels_colors.R
/usr/lib64/R/library/dendextend/tests/testthat/test-nleaves.R
/usr/lib64/R/library/dendextend/tests/testthat/test-pvclust_extract.R
/usr/lib64/R/library/dendextend/tests/testthat/test-rect.dendrogram.R
/usr/lib64/R/library/dendextend/tests/testthat/test-rotate.R
/usr/lib64/R/library/dendextend/tests/testthat/test-set.dendrogram.R
/usr/lib64/R/library/dendextend/tests/testthat/test-trim.R
/usr/lib64/R/library/dendextend/tests/testthat/test-unbranch.R
/usr/lib64/R/library/dendextend/tests/testthat/test-untangle.R
