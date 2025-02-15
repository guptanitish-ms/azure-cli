# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "monitor autoscale show-predictive-metric",
)
class ShowPredictiveMetric(AAZCommand):
    """Show predictive autoscale metric future data
    """

    _aaz_info = {
        "version": "2022-10-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.insights/autoscalesettings/{}/predictivemetrics", "2022-10-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.autoscale_setting_name = AAZStrArg(
            options=["--autoscale-setting-name"],
            help="The autoscale setting name.",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.aggregation = AAZStrArg(
            options=["--aggregation"],
            help="The list of aggregation types (comma separated) to retrieve.",
            required=True,
        )
        _args_schema.interval = AAZDurationArg(
            options=["--interval"],
            help="The interval (i.e. timegrain) of the query.",
            required=True,
        )
        _args_schema.metric_name = AAZStrArg(
            options=["--metric-name"],
            help="The names of the metrics (comma separated) to retrieve. Special case: If a metricname itself has a comma in it then use %2 to indicate it. Eg: 'Metric,Name1' should be **'Metric%2Name1'**",
            required=True,
        )
        _args_schema.metric_namespace = AAZStrArg(
            options=["--metric-namespace"],
            help="Metric namespace to query metric definitions for.",
            required=True,
        )
        _args_schema.timespan = AAZStrArg(
            options=["--timespan"],
            help="The timespan of the query. It is a string with the following format 'startDateTime_ISO/endDateTime_ISO'.",
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.PredictiveMetricGet(ctx=self.ctx)()
        self.post_operations()

    # @register_callback
    def pre_operations(self):
        pass

    # @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class PredictiveMetricGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Insights/autoscalesettings/{autoscaleSettingName}/predictiveMetrics",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "autoscaleSettingName", self.ctx.args.autoscale_setting_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "aggregation", self.ctx.args.aggregation,
                    required=True,
                ),
                **self.serialize_query_param(
                    "interval", self.ctx.args.interval,
                    required=True,
                ),
                **self.serialize_query_param(
                    "metricName", self.ctx.args.metric_name,
                    required=True,
                ),
                **self.serialize_query_param(
                    "metricNamespace", self.ctx.args.metric_namespace,
                    required=True,
                ),
                **self.serialize_query_param(
                    "timespan", self.ctx.args.timespan,
                    required=True,
                ),
                **self.serialize_query_param(
                    "api-version", "2022-10-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.data = AAZListType()
            _schema_on_200.interval = AAZStrType()
            _schema_on_200.metric_name = AAZStrType(
                serialized_name="metricName",
            )
            _schema_on_200.target_resource_id = AAZStrType(
                serialized_name="targetResourceId",
            )
            _schema_on_200.timespan = AAZStrType()

            data = cls._schema_on_200.data
            data.Element = AAZObjectType()

            _element = cls._schema_on_200.data.Element
            _element.time_stamp = AAZStrType(
                serialized_name="timeStamp",
                flags={"required": True},
            )
            _element.value = AAZFloatType(
                flags={"required": True},
            )

            return cls._schema_on_200


__all__ = ["ShowPredictiveMetric"]
