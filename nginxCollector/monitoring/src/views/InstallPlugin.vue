<template>
  <div class="mx-auto mt-lg-5" style="width: 60%;">
    <CRow>
      <CCol sm="12">
        <CCard>
          <CCardHeader
            class="p-4"
            color="info"
            style="font-size: 1.2rem; color: white"
          >
            Installing the plugin
          </CCardHeader>
          <CCardBody>
            <div class="m-4">
              <div class="docs-paragraph">
                <span>
                  In order to be able to use Nginx Collector to monitor your
                  infrastructure, you need to install the plugin and set up
                  nginx on each system that has to be checked.
                </span>
              </div>
              <div class="set-up-njs">
                <div class="title">
                  Installing and set up nginx
                </div>
                <br />
                <div class="name-step">
                  <div class="title-step">
                    1. Install modular njs as follow
                    <a
                      href="https://nginx.org/en/docs/njs/install.html"
                      target="_blank"
                      style="color: #077cdd; text-decoration: underline; cursor: pointer "
                      >njs modular</a
                    >
                  </div>
                </div>

                <div class="name-step">
                  <div class="title-step">
                    2. Create a new file
                    <span
                      style="font-style: italic; text-decoration: underline"
                    >
                      header.js
                    </span>
                    in
                    <span style="font-weight: bold; text-decoration: underline"
                      >/etc/nginx</span
                    >
                    and config as follow:
                  </div>
                  <div>
                    <vue-simple-markdown :source="source"></vue-simple-markdown>
                  </div>
                </div>
                <div class="name-step">
                  <div class="title-step">
                    3. Config
                    <span style="font-weight: bold; text-decoration: underline"
                      >/etc/nginx/nginx.conf</span
                    >
                    file as follow:
                  </div>
                  <div>
                    <vue-simple-markdown
                      :source="source1"
                    ></vue-simple-markdown>
                  </div>
                </div>
                <div class="name-step">
                  <div class="title-step">
                    4. Download install script using curl
                  </div>
                  <div>
                    <vue-simple-markdown
                      :source="source2"
                    ></vue-simple-markdown>
                  </div>
                </div>
              </div>
            </div>
          </CCardBody>
          <CCardFooter> </CCardFooter>
        </CCard>
      </CCol>
    </CRow>
  </div>
</template>

<script>
export default {
  data() {
    return {
      source:
        "```javascript\n" +
        "function headers(r) {\n" +
        "    var s = ''\n" +
        "    for (var h in r.headersIn) {\n" +
        "    \tif (s.length ) {\n" +
        "            s += ',';\n" +
        "        }\n" +
        '        s += "\'"+h+"\':\'"+r.headersIn[h] + "\'";\n' +
        "    }\n" +
        "    return s;\n" +
        "}\n" +
        "export default {headers};\n" +
        "```",
      source1:
        "```javacript\n" +
        "...\n" +
        "load_module modules/ngx_http_js_module.so;\n" +
        "load_module modules/ngx_stream_js_module.so;\n" +
        "...\n" +
        "\n" +
        "http {\n" +
        "    ...\n" +
        "    js_import header.js;\n" +
        "\n" +
        "    js_set $header header.headers;\n" +
        "    \n" +
        "    log_format json escape=none \"{'timestamp':'$msec',\"\n" +
        "                             \"'client':'$remote_addr',\"\n" +
        "                             \"'uri':'$request_uri',\"\n" +
        "                             \"'user_agent':'$http_user_agent',\"\n" +
        "                             \"'url':'$uri',\"\n" +
        "                             \"'request_method':'$request_method',\"\n" +
        "                             \"'request_time':'$request_time',\"\n" +
        "                             \"'upstream_connect_time':'$upstream_connect_time',\"\n" +
        "                             \"'upstream_header_time':'$upstream_header_time',\"\n" +
        "                             \"'upstream_response_time':'$upstream_response_time',\"\n" +
        "                             \"'status':$status,\"\t\n" +
        "                             \"'size':$body_bytes_sent,\"\n" +
        "                             \"'headers':{$header}}\";\t\n" +
        "\n" +
        "    access_log  /var/log/nginx/access.log  json;\n" +
        "\n" +
        "    ...\n" +
        "}\n" +
        "```",
      source2:
        "```javascript curl -L -O https://raw.githubusercontent.com/quanghuynguyen1902/nginxParse/master/plugin.py```"
    };
  }
};
</script>

<style lang="scss">
.docs-paragraph {
  max-width: 700px;
  font-size: 16px;
  margin: 15px 0;
}
.set-up-njs {
  .title {
    font-size: 18px;
    font-weight: bold;
    color: #333;
    font-family: "RobotoMedium", Arial, sans-serif;
  }
}
.name-step {
  font-size: 16px;
  margin-bottom: 20px;
}
</style>
