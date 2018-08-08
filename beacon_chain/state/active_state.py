from .attestation_record import AttestationRecord


class ActiveState():

    fields = {
        # Attestations that have not yet been processed
        'pending_attestations': [AttestationRecord],
        # Most recent EPOCH_LENGTH block hashes, older to newer
        'recent_block_hashes': ['hash32'],
    }
    defaults = {
        'pending_attestations': [],
        'recent_block_hashes': [],
    }

    def __init__(self, **kwargs):
        for k in self.fields.keys():
            assert k in kwargs or k in self.defaults
            setattr(self, k, kwargs.get(k, self.defaults.get(k)))

        if 'block_vote_cache' in kwargs:
            self.block_vote_cache = kwargs['block_vote_cache']
        else:
            self.block_vote_cache = {}

    @property
    def num_pending_attestations(self):
        return len(self.pending_attestations)
