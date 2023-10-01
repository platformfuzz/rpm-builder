FROM ghcr.io/platformfuzz/image-builder/stream8-devel:latest

COPY . .

RUN rpmdev-setuptree \
  & dnf install -y go

COPY ./yq.spec /root/rpmbuild/SPECS/

RUN /usr/bin/rpmbuild --ba /root/rpmbuild/SPECS/yq.spec \
  && dnf install -y /root/rpmbuild/RPMS/x86_64/yq-4.35.2-1.el8.x86_64.rpm
