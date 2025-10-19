import google.cloud.dlp
import os
from pydantic import BaseModel
from typing import List, Optional


dlp_client = google.cloud.dlp_v2.DlpServiceClient()


class Finding(BaseModel):
    """Represents a single sensitive data finding."""

    quote: str
    finding_type: str
    likelihood: str


class IdentifyResponse(BaseModel):
    """The response from the identify operation."""

    includes_finding: bool
    findings: Optional[List[Finding]] = None

    def __str__(self):
        if not self.findings:
            return ""
        else:
            findings_str = [
                f"Found: {finding.finding_type} with likelihood: {finding.likelihood}"
                for finding in self.findings
            ]

            return " ".join(findings_str)


def identify(content: str) -> IdentifyResponse:
    """Identifies sensitive data in a string.

    Args:
        content: The string to inspect.

    Returns:
        An IdentifyResponse object with the results of the inspection.
    """
    # Construct the item to inspect.
    item = {"value": content}

    # The info types to search for in the content. Required.
    info_types = [{"name": "FIRST_NAME"}, {"name": "LAST_NAME"}]

    # The minimum likelihood to constitute a match. Optional.
    min_likelihood = google.cloud.dlp_v2.Likelihood.LIKELIHOOD_UNSPECIFIED

    # The maximum number of findings to report (0 = server maximum). Optional.
    max_findings = 0

    # Whether to include the matching string in the results. Optional.
    include_quote = True

    # Construct the configuration dictionary. Keys which are None may
    # optionally be omitted entirely.
    inspect_config = {
        "info_types": info_types,
        "min_likelihood": min_likelihood,
        "include_quote": include_quote,
        "limits": {"max_findings_per_request": max_findings},
    }

    # Convert the project id into a full resource id.
    parent = f"projects/{os.getenv('GOOGLE_CLOUD_PROJECT')}"

    # Call the API.
    response = dlp_client.inspect_content(
        request={"parent": parent, "inspect_config": inspect_config, "item": item}
    )

    if response.result.findings:
        return IdentifyResponse(
            includes_finding=True,
            findings=[
                Finding(
                    quote=finding.quote,
                    finding_type=finding.info_type.name,
                    likelihood=finding.likelihood.name,
                )
                for finding in response.result.findings
            ],
        )
    else:
        return IdentifyResponse(includes_finding=False)
