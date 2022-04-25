import("./plist.slang").

defcon attestEnclavePublicKey(?EnclaveID, ?PublicKey) :-
{
    enclaveKey($EnclaveID, $PublicKey).
    label("receipt: attests public key for $EnclaveID").
}.

defpost postEnclavePublicKey(?EnclaveID, ?PublicKey) :-
    [attestEnclavePublicKey(?EnclaveID, ?PublicKey)].


defguard checkEnclavePublicKey(?EnclaveID) :-
    ?ReceiptToken := label("receipt: attests public key for $EnclaveID"),
{
    link($ReceiptToken).
}