from enum import Enum


class MESSAGE_TYPE(Enum):
    """Enum for different message types in the log."""

    ACCEPTED_PASSWORD = (
        r"Accepted\s+password\s+for\s+\S+\s+from\s+\S+\s+port\s+\d+\s+ssh2"
    )
    CONNECTION_CLOSED = r"Connection\s+closed\s+by\s+\S+\s+\[preauth\]"
    DID_NOT_RECEIVE = r"Did\s+not\s+receive\s+identification\s+string\s+from\s+\S+"
    TOO_MANY_AUTHENTICATION_FAILURES_ADMIN = r"Disconnecting:\s+Too\s+many\s+authentication\s+failures\s+for\s+admin\s+\[preauth\]"
    TOO_MANY_AUTHENTICATION_FAILURES_ROOT = r"Disconnecting:\s+Too\s+many\s+authentication\s+failures\s+for\s+root\s+\[preauth\]"
    NO_MORE_USER_AUTHENTICATION_METHODS = r"error:\s+Received\s+disconnect\s+from\s+\S+:\s+\S+:\s+No\s+more\s+user\s+authentication\s+methods\s+available.\s+\[preauth\]"
    FAILED_NONE = r"Failed\s+none.+"
    FAILED_PASSWORD = r"Failed\s+password.+"
    WRITE_FAILED = (
        r"fatal:\s+Write\s+failed:\s+Connection\s+reset\s+by\s+peer\s+\[preauth\]"
    )
    READ_FAILED = r"fatal:\s+Read\s+from\s+socket\s+failed:\s+Connection\s+reset\s+by\s+peer\s+\[preauth\]"
    INVALID_USER = r"input_userauth_request:.+"
    INVALID_USER_FROM = r"Invalid\s+user.+"
    REPEATED_MESSAGE = r"message\s+repeated\s+\S+\s+times:\s+\[(\s*)Failed\s+password\s+for\s+root\s+from\s+\S+\s+port\s+\S+\s+ssh2\]"
    PAM_AUTHENTICATION_FAILURE = r"PAM\s+\S+\s+more\s+authentication\s+failure(s?);\s+logname=\s+uid=\S+\s+euid=\S+\s+tty=ssh\s+ruser=\s+rhost=\S+"
    PAM_IGNORING_MAX_RETRIES = (
        r"PAM\s+service\(sshd\)\s+ignoring\s+max\s+retries;\s+\S+\s+>\s+\S+"
    )
    PAM_UNIX_AUTH_FAILURE = r"pam_unix\(sshd:auth\):\s+authentication\s+failure;\s+logname=\s+uid=\S+\s+euid=\S+\s+tty=ssh\s+ruser=\s+rhost=\S+"
    PAM_UNIX_AUTH_FAILURE_USER = r"pam_unix\(sshd:auth\):\s+authentication\s+failure;\s+logname=\s+uid=\S+\s+euid=\S+\s+tty=ssh\s+ruser=\s+rhost=\S+\s+user=\S+"
    PAM_UNIX_CHECK_PASS = r"pam_unix\(sshd:auth\):\s+check\s+pass;\s+user\s+unknown"
    PAM_UNIX_SESSION_CLOSED = (
        r"pam_unix\(sshd:session\):\s+session\s+closed\s+for\s+user\s+\S+"
    )
    PAM_UNIX_SESSION_OPENED = r"pam_unix\(sshd:session\):\s+session\s+opened\s+for\s+user\s+\S+\s+by\s+\(uid=\d+\)"
    RECEIVED_DISCONNECT = r".*Received\s+disconnect.*"
    BREAK_IN_ATTEMPT = r"(.+)POSSIBLE\s+BREAK-IN\s+ATTEMPT!"
    DISCONNECTING_TOO_MANY_AUTH_FAILURES = (
        r"Disconnecting:\s+Too\s+many\s+authentication\s+failures.+"
    )
    ERROR_OR_FATAL_OR_BAD_PROTOCOL = r"(fatal|error|Bad\s+protocol|Bad\s+packet).+"
    SERVER_LISTENING = r"Server\s+listening\s+on.+"
    UNKNOWN = r"others"


MESSAGE_INFO_TYPE = (
    MESSAGE_TYPE.ACCEPTED_PASSWORD.name,
    MESSAGE_TYPE.CONNECTION_CLOSED.name,
)

MESSAGE_WARNING_TYPE = (
    MESSAGE_TYPE.FAILED_PASSWORD.name,
    MESSAGE_TYPE.FAILED_NONE.name,
    MESSAGE_TYPE.READ_FAILED.name,
    MESSAGE_TYPE.WRITE_FAILED.name,
    MESSAGE_TYPE.REPEATED_MESSAGE.name,
)

MESSAGE_ERROR_TYPE = (
    MESSAGE_TYPE.DID_NOT_RECEIVE.name,
    MESSAGE_TYPE.TOO_MANY_AUTHENTICATION_FAILURES_ADMIN.name,
    MESSAGE_TYPE.TOO_MANY_AUTHENTICATION_FAILURES_ROOT.name,
    MESSAGE_TYPE.NO_MORE_USER_AUTHENTICATION_METHODS.name,
    MESSAGE_TYPE.ERROR_OR_FATAL_OR_BAD_PROTOCOL.name,
)

MESSAGE_CRITICAL_TYPE = (MESSAGE_TYPE.BREAK_IN_ATTEMPT.name,)
