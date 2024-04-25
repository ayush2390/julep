# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2024-04-20T14:32:07+00:00

from __future__ import annotations

from enum import Enum
from typing import Annotated, Any, Dict, List, Literal, Set
from uuid import UUID

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field, RootModel


class User(BaseModel):
    name: str | None = "User"
    """
    Name of the user
    """
    about: str | None = None
    """
    About the user
    """
    created_at: AwareDatetime | None = None
    """
    User created at (RFC-3339 format)
    """
    updated_at: AwareDatetime | None = None
    """
    User updated at (RFC-3339 format)
    """
    id: UUID
    """
    User id (UUID)
    """
    metadata: Dict[str, Any] | None = None
    """
    (Optional) metadata
    """


class FunctionParameters(BaseModel):
    """
    The parameters the functions accepts, described as a JSON Schema object.
    """

    model_config = ConfigDict(
        extra="allow",
    )


class FunctionDef(BaseModel):
    description: str | None = None
    """
    A description of what the function does, used by the model to choose when and how to call the function.
    """
    name: str
    """
    The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.
    """
    parameters: FunctionParameters
    """
    Parameters accepeted by this function
    """


class Type(str, Enum):
    """
    Whether this tool is a `function` or a `webhook` (Only `function` tool supported right now)
    """

    function = "function"
    webhook = "webhook"


class Tool(BaseModel):
    type: Type
    """
    Whether this tool is a `function` or a `webhook` (Only `function` tool supported right now)
    """
    function: FunctionDef
    """
    Function definition and parameters
    """
    id: UUID
    """
    Tool ID
    """


class Session(BaseModel):
    id: UUID
    """
    Session id (UUID)
    """
    user_id: UUID
    """
    User ID of user associated with this session
    """
    agent_id: UUID
    """
    Agent ID of agent associated with this session
    """
    situation: str | None = None
    """
    A specific situation that sets the background for this session
    """
    summary: str | None = None
    """
    (null at the beginning) - generated automatically after every interaction
    """
    created_at: AwareDatetime | None = None
    """
    Session created at (RFC-3339 format)
    """
    updated_at: AwareDatetime | None = None
    """
    Session updated at (RFC-3339 format)
    """
    metadata: Dict[str, Any] | None = None
    """
    Optional metadata
    """
    render_templates: bool | None = False
    """
    Render system and assistant message content as jinja templates
    """


class CreateSessionRequest(BaseModel):
    """
    A valid request payload for creating a session
    """

    user_id: UUID | None = None
    """
    (Optional) User ID of user to associate with this session
    """
    agent_id: UUID
    """
    Agent ID of agent to associate with this session
    """
    situation: str | None = None
    """
    A specific situation that sets the background for this session
    """
    metadata: Dict[str, Any] | None = None
    """
    Optional metadata
    """
    render_templates: bool | None = False
    """
    Render system and assistant message content as jinja templates
    """


class UpdateSessionRequest(BaseModel):
    """
    A valid request payload for updating a session
    """

    situation: str
    """
    Updated situation for this session
    """
    metadata: Dict[str, Any] | None = None
    """
    Optional metadata
    """


class UpdateUserRequest(BaseModel):
    """
    A valid request payload for updating a user
    """

    about: str
    """
    About the user
    """
    name: str
    """
    Name of the user
    """
    metadata: Dict[str, Any] | None = None
    """
    Optional metadata
    """


class Target(str, Enum):
    """
    Whether the suggestion is for the `agent` or a `user`
    """

    user = "user"
    agent = "agent"


class Suggestion(BaseModel):
    created_at: AwareDatetime | None = None
    """
    Suggestion created at (RFC-3339 format)
    """
    target: Target
    """
    Whether the suggestion is for the `agent` or a `user`
    """
    content: str
    """
    The content of the suggestion
    """
    message_id: UUID
    """
    The message that produced it
    """
    session_id: UUID
    """
    Session this suggestion belongs to
    """


class Role(str, Enum):
    """
    ChatML role (system|assistant|user|function_call|function)
    """

    user = "user"
    assistant = "assistant"
    system = "system"
    function_call = "function_call"
    function = "function"


class ChatMLMessage(BaseModel):
    role: Role
    """
    ChatML role (system|assistant|user|function_call|function)
    """
    content: str
    """
    ChatML content
    """
    name: str | None = None
    """
    ChatML name
    """
    created_at: AwareDatetime
    """
    Message created at (RFC-3339 format)
    """
    id: UUID
    """
    Message ID
    """


class Role1(str, Enum):
    """
    ChatML role (system|assistant|user|function_call|function|auto)
    """

    user = "user"
    assistant = "assistant"
    system = "system"
    function_call = "function_call"
    function = "function"
    auto = "auto"


class InputChatMLMessage(BaseModel):
    role: Role1
    """
    ChatML role (system|assistant|user|function_call|function|auto)
    """
    content: str
    """
    ChatML content
    """
    name: str | None = None
    """
    ChatML name
    """
    continue_: Annotated[bool | None, Field(False, alias="continue")]
    """
    Whether to continue this message or return a new one
    """


class Function(BaseModel):
    name: str
    """
    The name of the function to call.
    """


class NamedToolChoice(BaseModel):
    """
    Specifies a tool the model should use. Use to force the model to call a specific function.
    """

    type: Literal["function"] = "function"
    """
    The type of the tool. Currently, only `function` is supported.
    """
    function: Function


class ToolChoiceOption1(str, Enum):
    """
    `none` means the model will not call a function and instead generates a message. `auto` means the model can pick between generating a message or calling a function.

    """

    none = "none"
    auto = "auto"


class FunctionCallOption(BaseModel):
    """
    Specifying a particular function via `{"name": "my_function"}` forces the model to call that function.

    """

    name: str
    """
    The name of the function to call.
    """


class CompletionUsage(BaseModel):
    """
    Usage statistics for the completion request.
    """

    completion_tokens: int
    """
    Number of tokens in the generated completion.
    """
    prompt_tokens: int
    """
    Number of tokens in the prompt.
    """
    total_tokens: int
    """
    Total number of tokens used in the request (prompt + completion).
    """


class FinishReason(str, Enum):
    """
    The reason the model stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence, `length` if the maximum number of tokens specified in the request was reached, `content_filter` if content was omitted due to a flag from our content filters, `tool_calls` if the model called a tool, or `function_call` (deprecated) if the model called a function.
    """

    stop = "stop"
    length = "length"
    tool_calls = "tool_calls"
    content_filter = "content_filter"
    function_call = "function_call"


class Response(BaseModel):
    items: ChatMLMessage | None = None


class ChatResponse(BaseModel):
    """
    Represents a chat completion response returned by model, based on the provided input.
    """

    id: UUID
    """
    A unique identifier for the chat completion.
    """
    finish_reason: FinishReason
    """
    The reason the model stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence, `length` if the maximum number of tokens specified in the request was reached, `content_filter` if content was omitted due to a flag from our content filters, `tool_calls` if the model called a tool, or `function_call` (deprecated) if the model called a function.
    """
    response: List[List[ChatMLMessage] | Response]
    """
    A list of chat completion messages produced as a response.
    """
    usage: CompletionUsage
    jobs: Set[UUID] | None = None
    """
    IDs (if any) of jobs created as part of this request
    """


class Memory(BaseModel):
    agent_id: UUID
    """
    ID of the agent
    """
    user_id: UUID
    """
    ID of the user
    """
    content: str
    """
    Content of the memory
    """
    created_at: AwareDatetime
    """
    Memory created at (RFC-3339 format)
    """
    last_accessed_at: AwareDatetime | None = None
    """
    Memory last accessed at (RFC-3339 format)
    """
    timestamp: AwareDatetime | None = None
    """
    Memory happened at (RFC-3339 format)
    """
    sentiment: Annotated[float | None, Field(0, ge=-1.0, le=1.0)]
    """
    Sentiment (valence) of the memory on a scale of -1 to 1
    """
    id: UUID
    """
    Memory id (UUID)
    """
    entities: List[Dict[str, Any]]
    """
    List of entities mentioned in the memory
    """


class Type1(str, Enum):
    """
    Must be one of `"text"`, `"regex"` or `"json_object"`.
    """

    text = "text"
    json_object = "json_object"
    regex = "regex"


class ResponseFormat(BaseModel):
    """
    An object specifying the format that the model must output.

    Setting to `{ "type": "json_object" }` enables JSON mode, which guarantees the message the model generates is valid JSON.

    **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

    """

    type: Annotated[Type1 | None, Field("text", examples=["json_object"])]
    """
    Must be one of `"text"`, `"regex"` or `"json_object"`.
    """
    pattern: str | None = None
    """
    Regular expression pattern to use if `type` is `"regex"`
    """
    schema_: Annotated[Dict[str, Any] | None, Field({}, alias="schema")]
    """
    JSON Schema to use if `type` is `"json_object"`
    """


class Stop(RootModel[List[Any]]):
    root: Annotated[List[Any], Field(max_length=4, min_length=1)]
    """
    Up to 4 sequences where the API will stop generating further tokens.

    """


class Preset(str, Enum):
    """
    Generation preset name (problem_solving|conversational|fun|prose|creative|business|deterministic|code|multilingual)
    """

    problem_solving = "problem_solving"
    conversational = "conversational"
    fun = "fun"
    prose = "prose"
    creative = "creative"
    business = "business"
    deterministic = "deterministic"
    code = "code"
    multilingual = "multilingual"


class ChatSettings(BaseModel):
    frequency_penalty: Annotated[float | None, Field(0, ge=-1.0, le=1.0)]
    """
    (OpenAI-like) Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.
    """
    length_penalty: Annotated[float | None, Field(1, ge=0.0, le=2.0)]
    """
    (Huggingface-like) Number between 0 and 2.0. 1.0 is neutral and values larger than that penalize number of tokens generated. 
    """
    logit_bias: Dict[str, int] | None = None
    """
    Modify the likelihood of specified tokens appearing in the completion.

    Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token.

    """
    max_tokens: Annotated[int | None, Field(200, ge=1, le=16384)]
    """
    The maximum number of tokens to generate in the chat completion.

    The total length of input tokens and generated tokens is limited by the model's context length.

    """
    presence_penalty: Annotated[float | None, Field(0, ge=-1.0, le=1.0)]
    """
    (OpenAI-like) Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.
    """
    repetition_penalty: Annotated[float | None, Field(1, ge=0.0, le=2.0)]
    """
    (Huggingface-like) Number between 0 and 2.0. 1.0 is neutral and values larger than that penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.
    """
    response_format: ResponseFormat | None = None
    """
    An object specifying the format that the model must output.

    Setting to `{ "type": "json_object" }` enables JSON mode, which guarantees the message the model generates is valid JSON.

    **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

    """
    seed: Annotated[int | None, Field(None, ge=-1, le=9999)]
    """
    This feature is in Beta.
    If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same `seed` and parameters should return the same result.
    Determinism is not guaranteed, and you should refer to the `system_fingerprint` response parameter to monitor changes in the backend.

    """
    stop: str | Stop | None = None
    """
    Up to 4 sequences where the API will stop generating further tokens.

    """
    stream: bool | None = False
    """
    If set, partial message deltas will be sent, like in ChatGPT. Tokens will be sent as data-only [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format) as they become available, with the stream terminated by a `data: [DONE]` message. [Example Python code](https://cookbook.openai.com/examples/how_to_stream_completions).

    """
    temperature: Annotated[float | None, Field(0.75, examples=[0.75], ge=0.0, le=2.0)]
    """
    What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
    """
    top_p: Annotated[float | None, Field(1, examples=[1], gt=0.0, le=1.0)]
    """
    Defaults to 1 An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.  We generally recommend altering this or temperature but not both.
    """
    min_p: Annotated[float | None, Field(0.01, examples=[0.01], ge=0.0, lt=1.0)]
    """
    Minimum probability compared to leading token to be considered
    """
    preset: Preset | None = None
    """
    Generation preset name (problem_solving|conversational|fun|prose|creative|business|deterministic|code|multilingual)
    """


class Preset1(str, Enum):
    """
    Generation preset name (one of: problem_solving, conversational, fun, prose, creative, business, deterministic, code, multilingual)
    """

    problem_solving = "problem_solving"
    conversational = "conversational"
    fun = "fun"
    prose = "prose"
    creative = "creative"
    business = "business"
    deterministic = "deterministic"
    code = "code"
    multilingual = "multilingual"


class AgentDefaultSettings(BaseModel):
    frequency_penalty: Annotated[float | None, Field(0, ge=-2.0, le=2.0)]
    """
    (OpenAI-like) Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.
    """
    length_penalty: Annotated[float | None, Field(1, ge=0.0, le=2.0)]
    """
    (Huggingface-like) Number between 0 and 2.0. 1.0 is neutral and values larger than that penalize number of tokens generated. 
    """
    presence_penalty: Annotated[float | None, Field(0, ge=-1.0, le=1.0)]
    """
    (OpenAI-like) Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.
    """
    repetition_penalty: Annotated[float | None, Field(1, ge=0.0, le=2.0)]
    """
    (Huggingface-like) Number between 0 and 2.0. 1.0 is neutral and values larger than that penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.
    """
    temperature: Annotated[float | None, Field(0.75, examples=[0.75], ge=0.0, le=3.0)]
    """
    What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
    """
    top_p: Annotated[float | None, Field(1, examples=[1], ge=0.0, le=1.0)]
    """
    Defaults to 1 An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.  We generally recommend altering this or temperature but not both.
    """
    min_p: Annotated[float | None, Field(0.01, examples=[0.01], ge=0.0, lt=1.0)]
    """
    Minimum probability compared to leading token to be considered
    """
    preset: Preset1 | None = None
    """
    Generation preset name (one of: problem_solving, conversational, fun, prose, creative, business, deterministic, code, multilingual)
    """


class Doc(BaseModel):
    title: str
    """
    Title describing what this bit of information contains
    """
    content: str
    """
    Information content
    """
    id: UUID
    """
    ID of doc
    """
    created_at: AwareDatetime
    """
    Doc created at
    """
    metadata: Dict[str, Any] | None = None
    """
    optional metadata
    """


class CreateDoc(BaseModel):
    title: str
    """
    Title describing what this bit of information contains
    """
    content: str
    """
    Information content
    """
    metadata: Dict[str, Any] | None = None
    """
    Optional metadata
    """


class MemoryAccessOptions(BaseModel):
    recall: bool | None = True
    """
    Whether previous memories should be recalled or not
    """
    record: bool | None = True
    """
    Whether this interaction should be recorded in history or not
    """
    remember: bool | None = True
    """
    Whether this interaction should form memories or not
    """


class CreateToolRequest(BaseModel):
    type: Type
    """
    Whether this tool is a `function` or a `webhook` (Only `function` tool supported right now)
    """
    function: FunctionDef
    """
    Function definition and parameters
    """


class UpdateToolRequest(BaseModel):
    function: FunctionDef
    """
    Function definition and parameters
    """


class ResourceCreatedResponse(BaseModel):
    id: UUID
    created_at: AwareDatetime
    jobs: Set[UUID] | None = None
    """
    IDs (if any) of jobs created as part of this request
    """


class ResourceUpdatedResponse(BaseModel):
    id: UUID
    updated_at: AwareDatetime
    jobs: Set[UUID] | None = None
    """
    IDs (if any) of jobs created as part of this request
    """


class ResourceDeletedResponse(BaseModel):
    id: UUID
    deleted_at: AwareDatetime
    jobs: Set[UUID] | None = None
    """
    IDs (if any) of jobs created as part of this request
    """


class State(str, Enum):
    """
    Current state (one of: pending, in_progress, retrying, succeeded, aborted, failed)
    """

    pending = "pending"
    in_progress = "in_progress"
    retrying = "retrying"
    succeeded = "succeeded"
    aborted = "aborted"
    failed = "failed"
    unknown = "unknown"


class JobStatus(BaseModel):
    name: str
    """
    Name of the job
    """
    reason: str | None = None
    """
    Reason for current state
    """
    created_at: AwareDatetime
    """
    Job created at (RFC-3339 format)
    """
    updated_at: AwareDatetime | None = None
    """
    Job updated at (RFC-3339 format)
    """
    id: UUID
    """
    Job id (UUID)
    """
    has_progress: bool | None = False
    """
    Whether this Job supports progress updates
    """
    progress: Annotated[float | None, Field(0, ge=0.0, le=100.0)]
    """
    Progress percentage
    """
    state: State
    """
    Current state (one of: pending, in_progress, retrying, succeeded, aborted, failed)
    """


class PatchUserRequest(BaseModel):
    """
    A request for patching a user
    """

    about: str | None = None
    """
    About the user
    """
    name: str | None = None
    """
    Name of the user
    """
    metadata: Dict[str, Any] | None = None
    """
    Optional metadata
    """


class PatchAgentRequest(BaseModel):
    """
    A request for patching an agent
    """

    about: str | None = None
    """
    About the agent
    """
    name: str | None = None
    """
    Name of the agent
    """
    model: str | None = None
    """
    Name of the model that the agent is supposed to use
    """
    default_settings: AgentDefaultSettings | None = None
    """
    Default model settings to start every session with
    """
    metadata: Dict[str, Any] | None = None
    """
    Optional metadata
    """
    instructions: str | List[str] | None = None
    """
    Instructions for the agent
    """


class PatchSessionRequest(BaseModel):
    """
    A request for patching a session
    """

    situation: str | None = None
    """
    Updated situation for this session
    """
    metadata: Dict[str, Any] | None = None
    """
    Optional metadata
    """


class PartialFunctionDef(BaseModel):
    description: str | None = None
    """
    A description of what the function does, used by the model to choose when and how to call the function.
    """
    name: str | None = None
    """
    The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.
    """
    parameters: FunctionParameters | None = None
    """
    Parameters accepeted by this function
    """


class Agent(BaseModel):
    name: str
    """
    Name of the agent
    """
    about: str | None = ""
    """
    About the agent
    """
    created_at: AwareDatetime | None = None
    """
    Agent created at (RFC-3339 format)
    """
    updated_at: AwareDatetime | None = None
    """
    Agent updated at (RFC-3339 format)
    """
    id: UUID
    """
    Agent id (UUID)
    """
    default_settings: AgentDefaultSettings | None = None
    """
    Default settings for all sessions created by this agent
    """
    model: str
    """
    The model to use with this agent
    """
    metadata: Dict[str, Any] | None = None
    """
    Optional metadata
    """
    instructions: str | List[str] | None = None
    """
    Instructions for the agent
    """


class CreateUserRequest(BaseModel):
    """
    A valid request payload for creating a user
    """

    name: str | None = "User"
    """
    Name of the user
    """
    about: str | None = None
    """
    About the user
    """
    docs: List[CreateDoc] | None = None
    """
    List of docs about user
    """
    metadata: Dict[str, Any] | None = None
    """
    (Optional) metadata
    """


class CreateAgentRequest(BaseModel):
    """
    A valid request payload for creating an agent
    """

    name: str
    """
    Name of the agent
    """
    about: str | None = ""
    """
    About the agent
    """
    tools: List[CreateToolRequest] | None = None
    """
    A list of tools the model may call. Currently, only `function`s are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for.
    """
    default_settings: AgentDefaultSettings | None = None
    """
    Default model settings to start every session with
    """
    model: str | None = "julep-ai/samantha-1-turbo"
    """
    Name of the model that the agent is supposed to use
    """
    docs: List[CreateDoc] | None = None
    """
    List of docs about agent
    """
    metadata: Dict[str, Any] | None = None
    """
    (Optional) metadata
    """
    instructions: str | List[str] | None = None
    """
    Instructions for the agent
    """


class UpdateAgentRequest(BaseModel):
    """
    A valid request payload for updating an agent
    """

    about: str
    """
    About the agent
    """
    name: str
    """
    Name of the agent
    """
    model: str | None = None
    """
    Name of the model that the agent is supposed to use
    """
    default_settings: AgentDefaultSettings | None = None
    """
    Default model settings to start every session with
    """
    metadata: Dict[str, Any] | None = None
    """
    Optional metadata
    """
    instructions: str | List[str] | None = None
    """
    Instructions for the agent
    """


class ChatInputData(BaseModel):
    messages: Annotated[List[InputChatMLMessage], Field(min_length=1)]
    """
    A list of new input messages comprising the conversation so far.
    """
    tools: List[Tool] | None = None
    """
    (Advanced) List of tools that are provided in addition to agent's default set of tools. Functions of same name in agent set are overriden
    """
    tool_choice: NamedToolChoice | ToolChoiceOption1 | NamedToolChoice | None = None
    """
    Can be one of existing tools given to the agent earlier or the ones included in the request
    """


class ChatInput(ChatInputData, ChatSettings, MemoryAccessOptions):
    pass


class PatchToolRequest(BaseModel):
    function: PartialFunctionDef
    """
    Function definition and parameters
    """
