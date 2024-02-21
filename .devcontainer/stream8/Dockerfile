FROM ghcr.io/platformfuzz/image-builder/stream8-rpmbuild:latest

RUN rpmdev-setuptree \
  && dnf install -y git \
  && ln -s /root/rpmbuild rpmbuild
